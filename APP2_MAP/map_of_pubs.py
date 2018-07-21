# pubs location from xlsx file

import folium
from pandas import DataFrame
import pandas
from geopy.geocoders import Nominatim
nom=Nominatim()

address=nom.geocode("Szlak 3, 31-161, Krakow")
map=folium.Map(location=[address.latitude,address.longitude],zoom_start=6)

df_pubs=pandas.read_excel("Pubs.xlsx", sheet_name="SALA")

fg=folium.FeatureGroup(name="My Map")

for i in range(0, df_pubs.shape[0]):
     if nom.geocode(df_pubs.loc[i, "Address"]) is None:
         i = i + 1
     else:
         hotel=df_pubs.loc[i, "Name"]
         lat=nom.geocode(df_pubs.loc[i, "Address"]).latitude
         lon=nom.geocode(df_pubs.loc[i, "Address"]).longitude
         fg.add_child(folium.Marker(location=[lat,lon],popup=hotel,icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("C:/Users/Ania/PycharmProjects/udemy/APP2_MAP/Map_pubs.html")






