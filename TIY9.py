import csv
from datetime import datetime
from plotly.graph_objs import Layout
from plotly import offline

filename = "data/world_fires_1_day.csv"

try:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        lat_index = header_row.index("latitude")
        lon_index = header_row.index("longitude")
        date_index = header_row.index("acq_date")
        frp_index = header_row.index('frp')


        dates, lats, lons, frps = [], [], [], []

        for row in reader:
            try:
                current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
                lat = float(row[lat_index])
                lon = float(row[lon_index])
                frp = float(row[frp_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            except IndexError:
                print(f"Missing data for a date. Unknown")
            else:
                dates.append(current_date)
                lats.append(lat)
                lons.append(lon)
                frps.append(frp)

    # Map the fires
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [frp/100 for frp in frps],
            'color': frps,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Fire Radiative Power'},
        },
    }]
    my_layout = Layout(title=f"{filename}")

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='htmls/world_fires.html')
except FileNotFoundError:
    print("The file that you provided could not be found. Please enter valid data.")
