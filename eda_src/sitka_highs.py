from pathlib import Path
import csv

path = Path('./data/chapter_16/the_csv_file_format/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)