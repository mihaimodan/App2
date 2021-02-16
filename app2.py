import folium

map = folium.Map(location = [44.719351, 24.9279223], zoom_start = 6, tiles = "OpenStreetMap" ) #Current location when writing this

#Personalizing the map object with .add_child.
map.add_child(folium.Marker(location = [44.7, 24.9], popup ="Peek-a-boo!", icon =folium.Icon(color = "blue")))

map.save("Map test.html")