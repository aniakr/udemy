from pandas import DataFrame
import pandas

df_ICAP=pandas.read_excel("python.xlsx",sheetname=1)

df_ICAP.loc[0,"Q1"]

# (note that in loc 0 is interpreted as a label of the index,
# and never as an integer position along the index).

# print(df_ICAP.loc[:,"Q3"])
# print(list(df_ICAP.loc[:,"Q3"]))

# print(df_ICAP.iloc[1:4,1:4])
#
# print(df_ICAP.ix[1:4,"Q3"])
# ix is not recommended but loc worked with both labels and indexes
# as well as iloc - why??

# print(df_ICAP.drop("Q3",1))
# print(df_ICAP.drop(df_ICAP.index[0:2],0))
# df.index and df.columns - zwraca serie z nazwami kolumn/rzedow

# adding a column - in place

df_ICAP["Q4"]=df_ICAP.shape[0]*[100]

# df.shape - wymiary

df_ICAP["Q4"]=df_ICAP["Q4"]*2

# adding a row - transpose twice
# df.T

for i in range(0,df_ICAP.shape[0]):
    df_ICAP.loc[i, "Q4"] = df_ICAP.loc[i,"Q4"] + i
