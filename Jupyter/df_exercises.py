from pandas import DataFrame
import os
import pandas
print(os.listdir())

df_own=pandas.DataFrame([[1,2,4],[56,1,0]],columns=["column1","column2","column3"])
# df_csv=pandas.read_csv("supermarkets.csv")
# df_json=pandas.read_json("supermarkets.json")
# df_xlsx=pandas.read_excel("supermarkets.xlsx", sheetname=0)
# df_txt_commas=pandas.read_csv("supermarkets-commas.txt")
# df_txt_scolons=pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
# df_web=pandas.read_csv("http://www.pythonhow.com/supermarkets.csv")

print(df_own.max().max())
print(df_own.column1)