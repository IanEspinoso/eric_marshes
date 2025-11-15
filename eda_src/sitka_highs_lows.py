from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('./data/chapter_16/the_csv_file_format/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and maximum and minimum temperatures
dates, highs, lows, rains = [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[7])
        low = int(row[8])
        rain = float(row[5])
    except ValueError:
        print(f"Missing rain data on {current_date}")
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
    rains.append(rain)

# Plots the maximum and minimum temperatures
plt.style.use('fast')
fig, ax1 = plt.subplots()
ax1.plot(dates, highs, color='red', alpha=0.5)
ax1.plot(dates, lows, color='blue', alpha=0.5)
ax1.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Instantiate a second axis that shares the same x-axis
ax2 = ax1.twinx() 
ax2.scatter(dates, rains, label='Precipitation', 
            alpha=0.25, edgecolors='black', marker='o', s=32)

# Formats the chart
ax1.set_title("Daily Climate, 2021", fontsize=24)
ax1.set_xlabel('', fontsize=16)
fig.tight_layout() # to avoid clipping from either side
ax1.set_ylabel("Temperature (F)", fontsize=16)
ax2.set_ylabel("Precipitation (in)", fontsize=16)
ax1.tick_params(labelsize=16)

plt.show()