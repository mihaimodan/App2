import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = data["LAT"].to_list()
lon = data["LON"].to_list()
elev = data["ELEV"].to_list()

#create a function that sets conditionals for later use in marker color.
def color_marker(elevation):     
    if elevation < 1000:
        return "green"  
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [38, -99], zoom_start = 6, tiles = "OpenStreetMap" ) #This gives us the initial location, zoom level, map background when opening the html.

fg1 = folium.FeatureGroup(name = "Volcanoes") #FeatureGroup acts as a layer.
fg2 = folium.FeatureGroup(name = "Population Density")

#Personalizing the map object with .add_child. Adding circle markers.
for lt, ln, elv in zip(lat, lon, elev):
    fg1.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = "Elevation: %s m" %elv, fill_color = color_marker(elv), color = "grey", fill= True, fill_opacity = 0.7))


#Adding a new layer of polygons with the data parameter. By adding the style_function parameter, we changed the color by population density.
fg2.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = "utf-8-sig").read(), style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <= 5000000 else 'yellow' if 5000000 < x['properties']['POP2005'] < 15000000 else 'orange' if 15000000 < x['properties']['POP2005'] <=40000000 else 'red'}))

map.add_child(fg1)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map.html")   