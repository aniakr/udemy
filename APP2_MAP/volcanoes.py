# my version of folium map

import folium
from pandas import DataFrame
import pandas
from geopy.geocoders import Nominatim

nom=Nominatim()
df_volcanoes=pandas.read_csv("Volcanoes_USA.txt")

def volcano_color(elevation):
    if elevation <= 1500:
        return "green"
    elif 1500 < elevation <= 3000:
        return "orange"
    else:
        return "red"

# for exercising purposes usage of two different methods:

latitudes=df_volcanoes["LAT"].tolist()
longitudes=list(df_volcanoes["LON"])
elevations=df_volcanoes["ELEV"].tolist()
names=list(df_volcanoes["NAME"])

map=folium.Map(location=[38,-120],zoom_start=5)

fgv=folium.FeatureGroup(name="Volcanoes")

for lat, lon, name, elev in zip(latitudes,longitudes, names, elevations):
    # popup1 = str(folium.Popup(html=name, parse_html=True))+"\n" + str(elev)+" m" - this part is not working
    fgv.add_child(folium.CircleMarker(location=(lat,lon),radius=7,popup=str(elev)+ " m",
    fill=True,fill_color=volcano_color(elev), color="grey",fill_opacity=0.5))

# without feature group it would create 62 layers
# but with GeoJson feature group are not necessary. we could add child directly to the map

fgp=folium.FeatureGroup(name="Population")

map.add_child(folium.GeoJson
             (data=open("world.json",'r',encoding='utf-8-sig').read(),
              style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange'
              if 10000000 <= x['properties']['POP2005'] < 40000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map_volcanoes.html")