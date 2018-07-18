from geopy.geocoders import Nominatim
nom=Nominatim()

from pandas import DataFrame
import pandas

# df_knajpy=pandas.read_excel("Knajpy.xlsx",sheetname="SALA")
# df_knajpy["GEO"]=""
#
# print(nom.geocode(df_knajpy.loc[4,"Address"]).latitude)
#
# for i in range(0,df_knajpy.shape[0]):
#     print(nom.geocode(df_knajpy.loc[i,"Address"]))
#
#
#
#
# # for i in range(0,df_knajpy.shape[0]):
# #     df_knajpy.loc[i,"GEO"]=nom.geocode(df_knajpy.loc[i,"Address"]).longitude
#
#
#
# geo=nom.geocode("Szlak 3/7, 31-161, Krakow")
# geo.latitude
# geo.longitude


df_spr=pandas.read_csv("supermarkets.csv")
df_spr["Latitude"] = ""
df_spr["Longitude"] = ""

for i in range(0,df_spr.shape[0]):
     address=", ".join(list(df_spr.iloc[i,1:5]))
     geo=nom.geocode(address)
     if geo is None:
          i=i+1
     else:
          lat=geo.latitude
          lon=geo.longitude
          df_spr.iloc[i,7]=lat
          df_spr.iloc[i,8]=lon

df_spr["Full address"]=df_spr["Address"]+", "+df_spr["City"]+", "+df_spr["State"]+", "+df_spr["Country"]
df_spr["Coordinates"]=df_spr["Full address"].apply(nom.geocode)
df_spr["Latitude2"]=df_spr["Coordinates"].apply(lambda x:x.latitude if x != None else None)
df_spr["Longitude2"]=df_spr["Coordinates"].apply(lambda x:x.longitude if x != None else None)

print(df_spr)


