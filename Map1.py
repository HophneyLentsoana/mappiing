import pandas
import folium
from folium.map import FeatureGroup, Icon, Popup

data =pandas.read_csv("Volcanoes.csv")
lat =list(data["LAT"])
lon =list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

fgv =FeatureGroup(name ="Volcanoes")


for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius= 6, popup= str(el)+"m",fill_color = color_producer(el), colour = 'grey', fill_opacity =0.7))

fgp =FeatureGroup(name ="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding= 'utf-8-sig').read(),
style_function=lambda x: {'fillColor':'grren' if x['properties']['POP2005'] <10000000 
else 'orange' if 10000000 <=x['properties']['POP2005'] <20000000  else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
