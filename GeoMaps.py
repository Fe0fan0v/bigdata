import folium
import pandas as pd
volcanos = folium.Map(location=[37.296933, -121.9574983],
                      zoom_start=8,
                      tiles='CartoDB dark_matter')

data = pd.read_csv('vulc.txt')
lat = data['LAT']
lon = data['LON']
elev = data['ELEV']


def color_change(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


for lat, lon, elev in zip(lat, lon, elev):
    folium.Marker(location=[lat, lon],
                  icon=folium.Icon(color=color_change(elev))
                  ).add_to(volcanos)
volcanos.save('volc.html')

# \\itcube\Share\Python
