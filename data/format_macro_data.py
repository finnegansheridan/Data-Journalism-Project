import json
import csv

# Create the dictionary here
borough_data = {}
file = open("data/data_original.csv", "r", newline="")
reader = csv.reader(file)
header = next(reader)  

for row in reader:
    borough, year, date_collected, * data_values = row
    if borough not in borough_data:
        borough_data[borough] = {}
    if year not in borough_data[borough]:
        borough_data[borough][year] = {}
    borough_data[borough][year][date_collected] = data_values

#Save the json object to a file
f2 = open("macro.json", "w")
json.dump(borough_data, f2, indent=4)

f2.close()
