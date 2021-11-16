#%%
import pandas as pd

#%%
mta_df= pd.read_csv("http://web.mta.info/developers/data/nyct/turnstile/turnstile_211113.txt")
print(mta_df.columns)

# %%
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
mta_df.Date