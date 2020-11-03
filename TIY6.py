import json

from plotly.graph_objs import Layout
from plotly import offline

# Explore the structure of the data
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])  # Getting the magnitude of the earthquake from our data.
    lons.append(eq_dict['geometry']['coordinates'][0])  # gets the longitude
    lats.append(eq_dict['geometry']['coordinates'][1])  # gets the latitude
    hover_texts.append(eq_dict['properties']['title'])  # Gets the title/location (in name) of the earthquake.


# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='htmls/global_earthquakes.html')
