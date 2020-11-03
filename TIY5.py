import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_full.csv"

try:
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        maxtemp_index = header_row.index("TMAX")
        mintemp_index = header_row.index("TMIN")
        date_index = header_row.index("DATE")
        station_index = header_row.index("STATION")
        name_index = header_row.index("NAME")

        dates, highs, lows = [], [], []

        station = ""
        name = ""

        for row in reader:
            try:
                station = row[station_index]
                name = row[name_index]
                current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
                high = int(row[maxtemp_index])
                low = int(row[mintemp_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red', alpha=0.5)
        ax.plot(dates, lows, c='blue', alpha=0.5)

        # Fill between the two plots.
        plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

        # Limit y-axis
        plt.ylim((0, 150))

        # Format the plot

        plt.title(f"Daily high and low temperatures\n{station} - {name}", fontsize=20)
        plt.xlabel("", fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
except FileNotFoundError:
    print("The file that you provided could not be found. Please enter valid data.")
