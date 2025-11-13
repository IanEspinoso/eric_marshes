from pathlib import Path
import csv

path = Path('./data/chapter_16/the_csv_file_format/weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and maximum and minimum temperatures
for index, column_header in enumerate(header_row):
    print(index, column_header)