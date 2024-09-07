import pandas as pd
import csv
import os

df0 = pd.read_csv("quantium-starter-repo\data\daily_sales_data_0.csv")

df1 = pd.read_csv("quantium-starter-repo\data\daily_sales_data_1.csv")

df2 = pd.read_csv("quantium-starter-repo\data\daily_sales_data_2.csv")

data = [df0, df1, df2]
df = pd.concat(data, ignore_index=True)

df["price"] = df["price"].replace('[\$\,\.]', '', regex=True).apply(int)
df["sales"] = df["price"]*df["quantity"]

cleaned_df = df[df["product"] == "pink morsel"]
cleaned_df = cleaned_df[["sales","date","region"]]
print(cleaned_df)

os.makedirs('quantium-starter-repo', exist_ok=True)  
cleaned_df.to_csv('quantium-starter-repo/data.csv')  
