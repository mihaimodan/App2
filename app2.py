import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = data["LAT"].to_list()
lon = data["LON"].to_list()

map = folium.Map(location = [43, 25], zoom_start = 6, tiles = "OpenStreetMap" ) #Current location when writing this

fg = folium.FeatureGroup(name = "My Map")

#Personalizing the map object with .add_child. Adding a marker.

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location = [lt, ln], popup ="Peek-a-boo!", icon =folium.Icon(color = "green")))

map.add_child(fg)


map.save("Map test.html")   