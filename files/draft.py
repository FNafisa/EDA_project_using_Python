#%%
import sqlite3
# %%
con= sqlite3.connect("data/IndianPremierLeague2008_2016.sqlite")
#%%
cur = con.cursor()
x=cur.execute("SELECT name FROM sqlite_master WHERE type='table';")

# %%
for row in cur.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)



# %%
con.close()
# %%

# testing read_csv() in a different file

df_test =pd.read_csv("data/csv files/city.csv")
df_test.columns
# %%
mask = ~df_test["population"].isna()
mask


# %%
# check_missing_values_in_every_column(df_test)



# %%

plt.bar(df_test["population"],new_x = np.arange(20));