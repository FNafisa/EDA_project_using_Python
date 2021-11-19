#%%
from matplotlib import colors
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.io.pytables import Term

#%%
#import the data we want from the desired website and store it in a dataframe called mta_df
# mta_df= pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_211113.txt") #2021, 3rd Nov
mta_df= pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_141018.txt") #2010, 5th May
ev_df= pd.read_csv("data\csv files\ElectricCarData_Clean.csv")
#%%
# this method gives a glimps of our dataframe



#%%
# %%
# change the columns names to more convenient ones

#             {   ! note that exit was actully something 
#                   like this : "EXITS                        " and i changed it to be like this: "Exits" 
#                   as demonstrated below :)                                                                 }
#

mta_df.rename(columns={
    "UNIT":"Unit",
    "STATION":"Station",
    "LINENAME": "Linename",
    "DIVISION": "Division",
    "DATE":"Date",
    "ENTRIES":"Entries",
    "EXITS                                                               ":"Exits",

    }, inplace=True)


# %%

# check on the new naming of the columns
print(mta_df.columns,"\n+++++++++++++++++++++++++++\n")
#%%
print(mta_df.Date)



#%%

#    trying to detect missing values :(
#

#                                        first...
#                               define some useful functions
#   {_______________________________________________________________________________________}
#                                           | |
#                                           | | 
#                                           | |
#                                           | |
#                                          _| |_
#                                          \   /
#                                           \ /
#                                            V


# # this method gives a glimps of our dataframe
# def glimps(df):
#     print(
#         str(df.info())
#         ,"\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
#         ,"the shape of your dataframe is {} column/s and {} row/s ".format(df.shape[1],df.shape[0]).upper()
#         ,"\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
#         ,df.columns
#         )

#this method checks missing values in every column and print the rows containing those missing values
def check_missing_values_in_every_column(df):
    for column in df:
        print(
             "\n"
            ,df[str(column)].isna().value_counts()
            ,"\n-------------------------------"
            )


#this method drops missing values in every column, but unfortunately is seems to be not working at all :(
def drop_missing_values_for_each_column(df):
    for column in df:
        df.dropna(subset=[str(column)], inplace=True)



#              use our defined functions
#%%
# mta_df.info()
#%%
check_missing_values_in_every_column(ev_df)
#%%
drop_missing_values_for_each_column(ev_df)
#%%
check_missing_values_in_every_column(ev_df)
#%%



# %%

#the next three cells are some practice on matplotlib package

(
    plt.plot(mta_df["Entries"],"g"), plt.plot(mta_df["Exits"], linestyle= ":", color="r", linewidth= 2)
    ,plt.title("Entries & Exits", fontsize= 20, loc= "left", color= "grey")
    ,plt.xlabel("x axis")
    ,plt.ylabel("y axis")
    ,plt.grid()
    ,plt.xticks(np.linspace(0,200000,4), ["Mar","Jun","Sep","Dec"], family="fantasy")
    ,plt.yticks(np.linspace(1,2,3))
);
# %%
(
    plt.plot(mta_df["Entries"],"g"), plt.plot(mta_df["Exits"], linestyle= ":", color="r", linewidth= 2)
    ,plt.title("Entries & Exits", fontsize= 20, loc= "left", color= "grey")
    ,plt.xlabel("x axis")
    ,plt.ylabel("y axis")
    ,plt.grid()
    ,plt.xticks(np.linspace(0,200000,4), ["Mar","Jun","Sep","Dec"], family="fantasy")
    ,plt.yticks(np.linspace(1,2,3))
);
#%%
(
    plt.scatter(mta_df["Entries"],mta_df["Exits"])
    ,plt.title("Entries & Exits", fontsize= 20, loc= "left", color= "grey")
    ,plt.xlabel("x axis")
    ,plt.ylabel("y axis")
    ,plt.grid()
    ,plt.xticks(np.linspace(0,200000,4), ["Mar","Jun","Sep","Dec"], family="fantasy")
    ,plt.yticks(np.linspace(1,2,3))
);
# %%





