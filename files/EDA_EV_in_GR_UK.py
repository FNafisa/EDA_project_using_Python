#%% ----------------------------------------------------------------------------------
# setting up and import the required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.utils import percentiles
# %%
%matplotlib inline
sns.set()


# %% ----------------------------------------------------------------------------------
# import our dataset and store it in a dataframe
df_ev= pd.read_csv("data\csv files\ev_cars.csv")



# %% ----------------------------------------------------------------------------------
# Rename the columns to more convenient names
df_ev.rename(
    columns={
        "Acceleration":"Acceleration(sec)"
        ,"TopSpeed":"Top_Speed(km/h)"
        ,"Range":"Range(km)"
        ,"Efficiency":"Efficiency(Wh/km)"
        ,"FastChargeSpeed":"Fast_Charge_Speed(km/h)"
        ,"PriceinGermany":"Price_in_Germany(USD)"
        ,"PriceinUK":"Price_In_UK(USD)"
        } 
    ,inplace=True)



# %% ----------------------------------------------------------------------------------
# get rid of the measuring units after emphisizing that in the columns
# and them change data type of the price column to be float instead of int,
# so we can convert it from Euro and  UK Pound to US dollars
# in a new different column


# remove measuring units and them change data type of the price column to be float instead of int
df_ev.loc[:,"Acceleration(sec)":"Fast_Charge_Speed(km/h)"]= df_ev.loc[:,"Acceleration(sec)":"Fast_Charge_Speed(km/h)"].replace(
                                                                                                                            {'sec':'', "km/h":"", "km":"", "Wh/":"", "-":None} 
                                                                                                                            ,regex=True
                                                                                                                            ).astype(float)

# change text elements data type to be String 
df_ev["Name"]= df_ev["Name"].astype(str)
df_ev["Subtitle"]= df_ev["Subtitle"].astype(str)
df_ev["Drive"]= df_ev["Drive"].astype(str)
#%%
# remove commas and currency signs from our dataset and convert currancy to USD
df_ev["Price_in_Germany(USD)"]= df_ev["Price_in_Germany(USD)"].replace('[\€,]', '', regex=True).astype(float) * 1.14
df_ev["Price_In_UK(USD)"]= df_ev["Price_In_UK(USD)"].replace('[\£,]', '', regex=True).astype(float) * 1.35

#%% ----------------------------------------------------------------------------------
# handle the NaN values by dropping the rows that contain them in the prices columns only and fill the ones in the fast charge speed column with the appropriate value (ie. median or mean)
df_ev.isna().sum()
df_ev.dropna(subset=["Price_in_Germany(USD)","Price_In_UK(USD)"], inplace=True)
# %% 
#and fill the ones in the fast charge speed column with the appropriate value (ie. median or mean)
fast_charge_speed_median_and_mean = (df_ev["Fast_Charge_Speed(km/h)"].median(),df_ev["Fast_Charge_Speed(km/h)"].mean())
fast_charge_speed_median_and_mean
df_ev["Fast_Charge_Speed(km/h)"].fillna(fast_charge_speed_median_and_mean[1], inplace=True)


#---------------------------{   !!!!!!!!! CONGRATUKATIONS !!!!!!!!!!  }------------------------------------#
############################################################################################################
#                    now the dataset is cleaned and ready to be exported for any further                   #
#                    analysis, and because I don't want to alter it while continueing this                 #
#                    analysis I decided to to make a copy of it and store in a deffirent                   #
#                    variable named df_test :)                                                             #
############################################################################################################

# %% ----------------------------------------------------------------------------------
# export the dataset 
df_ev.to_csv("data\csv files\ev_cars_CLEANED.csv", index=False)


#%% ----------------------------------------------------------------------------------
# copy and store the dataset in df_test
df_test= df_ev.copy(deep=True)

#%% ----------------------------------------------------------------------------------
# these graphs are to know the nature of EV prices in Gr and UK 
(
    sns.boxplot(data=df_test.loc[:,"Price_in_Germany(USD)":"Price_In_UK(USD)"]).set_title("Price Comparison of EV in Germany and UK in USD")
);
# %%
(
    plt.plot(df_test["Price_in_Germany(USD)"],"blue"), plt.plot(df_test["Price_In_UK(USD)"], linestyle= ":", color="orange", linewidth= 2)
    ,plt.title("Price Comparison of EV in Germany and UK in USD", fontsize= 16, loc= "center")
    ,plt.xlabel("CARS")
    ,plt.ylabel("PRICES IN USD")
    ,plt.xticks([])
);



# %% ----------------------------------------------------------------------------------
# begin analysis for Family Car
# Family Car main properties based on our dataset:
#   Name, Acceleration(sec), Top_Speed(km/h), Range(km),	Efficiency(Wh/km),	Fast_Charge_Speed(km/h), NumberofSeats, Price_in_Germany(USD),	Price_In_UK(USD)

# now we will creat a new dataframe for this very purpose
df_FC= df_test.copy(deep=True)

#%% 
# then drop the unnecessery columns 
df_FC= df_FC.drop(['Subtitle', 'Drive'], axis = 1)
# %%
# what makes a car realy conveneint for a family is its capacity a.k.a number of seats and thats 
# why we will create a new column to categorize the cars into to categories, is/ isn't a family car

# first we create a local function for this purpose where we assign True value to cars with
# 5 seats as it is a Family Car, and False for the others
def is_or_isnt_Family_Car(seats):
    if seats >= 5:
        return True
    else:
        return False
#%%
# we apply that local function to create the new column
df_FC["Family_car"]= df_FC["NumberofSeats"].apply(is_or_isnt_Family_Car)
#%%
plt.pie(df_FC["Family_car"].value_counts(),labels=['Family Car','Not Family Car'],pctdistance=1.1);
# %%
print("thx... <3")
# %%
