#%% ----------------------------------------------------------------------------------
# setting up and import the required packages
from os import stat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn import tree
# from sklearn.metrics import accuracy_score
# %%
%matplotlib inline
sns.set()


# %% ----------------------------------------------------------------------------------
# import our dataset and store it in a dataframe
df_ev= pd.read_csv("data\csv files\ev_cars.csv")


#%% ----------------------------------------------------------------------------------
# check on our data set and its first rows
df_ev.info()
#%%
df_ev.head(n=3)
#%%
df_ev.PriceinGermany.describe()


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
# get rid of the measuring units in after emphisizing that in the columns
# and them change data type of the price column to be float instead of int,
# so we can convert it from Euro and  UK Pound to US dollars
# in a new different column
# remove measuring units
df_ev.loc[:,"Acceleration(sec)":"Fast_Charge_Speed(km/h)"]= df_ev.loc[:,"Acceleration(sec)":"Fast_Charge_Speed(km/h)"].replace(
                                                                                                                            {'sec':'', "km/h":"", "km":"", "Wh/":"", "-":None} 
                                                                                                                            ,regex=True
                                                                                                                            ).astype(float)
df_ev["Name"]= df_ev["Name"].astype(str)
df_ev["Subtitle"]= df_ev["Subtitle"].astype(str)
df_ev["Drive"]= df_ev["Drive"].astype(str)
#%%
# remove commas and currency signs from our dataset and convert currancy to USD
df_ev["Price_in_Germany(USD)"]= df_ev["Price_in_Germany(USD)"].replace('[\€,]', '', regex=True).astype(float) * 1.14
df_ev["Price_In_UK(USD)"]= df_ev["Price_In_UK(USD)"].replace('[\£,]', '', regex=True).astype(float) * 1.35


#%% ----------------------------------------------------------------------------------
# define some dataframes to work with
df_ev_ger= df_ev.drop("Price_In_UK(USD)", axis="columns")
df_ev_uk= df_ev.drop("Price_in_Germany(USD)", axis="columns")

df_test= df_ev.copy(deep=True)


#%% ----------------------------------------------------------------------------------
# handle the NaN values



# %%
df_test.isna().sum()
df_test.dropna(subset=["Price_In_UK(USD)"], inplace=True)

# %%
fast_charge_speed_median_and_mean = (df_test["Fast_Charge_Speed(km/h)"].median(),df_test["Fast_Charge_Speed(km/h)"].mean())
fast_charge_speed_median_and_mean
# %%
df_test["Fast_Charge_Speed(km/h)"].fillna(fast_charge_speed_median_and_mean[1], inplace=True)
# %%
def fast_not_fast(speed):
    if speed > 150:
        return 'fast'
    else:
        return 'not fast'
#%%
# we can use this also to create categories such : Family Cars
df_test["fast/not_fast"]= df_test["Top_Speed(km/h)"].apply(fast_not_fast)
# %%
the_mean_priceGer_for_every_Drive_type= df_test.groupby("Drive")["Price_in_Germany(USD)"].mean().sort_values(ascending= False)
# %%
plt.hist(
    df_test["Range(km)"],
    bins= 30,
);
#%%
sns.histplot(
    df_test["Range(km)"],
    kde= True,
    bins= 8,
);
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
# %%


