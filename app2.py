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
    
map = folium.Map(location = [38, -99], zoom_start = 6, tiles = "OpenStreetMap" ) #Current location when writing this

fg = folium.FeatureGroup(name = "My Map") #FeatureGroup acts as a layer.

#Personalizing the map object with .add_child. Adding a marker.

for lt, ln, elv in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = "Elevation: %s m" %elv, fill_color = color_marker(elv), color = "grey", fill= True, fill_opacity = 0.7))

map.add_child(fg)


map.save("Map test.html")   