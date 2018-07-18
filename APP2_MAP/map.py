import folium
from pandas import DataFrame
import pandas
from geopy.geocoders import Nominatim
nom=Nominatim()

address=nom.geocode("Szlak 3, 31-161, Krakow")
map=folium.Map(location=[address.latitude,address.longitude],zoom_start=6)

df_knajpy=pandas.read_excel("C:/Users/Ania/PycharmProjects/test1/udemy/Jupyter/Knajpy.xlsx",sheet_name="SALA")

fg=folium.FeatureGroup(name="My Map")

# for i in range(0,df_knajpy.shape[0]):
#     if nom.geocode(df_knajpy.loc[i,"Address"]) is None:
#         i = i + 1
#     else:
#         hotel=df_knajpy.loc[i,"Name"]
#         lat=nom.geocode(df_knajpy.loc[i,"Address"]).latitude
#         lon=nom.geocode(df_knajpy.loc[i,"Address"]).longitude
#         fg.add_child(folium.Marker(location=[lat,lon],popup=hotel,icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("C:/Users/Ania/PycharmProjects/test1/udemy/APP2_MAP/Map2.html")






