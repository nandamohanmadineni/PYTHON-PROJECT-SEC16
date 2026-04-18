# storage/csv_store.py  week-8
import csv

with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Ram", 90])