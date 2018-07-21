from geopy.geocoders import Nominatim
nom=Nominatim()
from pandas import DataFrame
import pandas

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


