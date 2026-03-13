import csv

total_fare = 0
count = 0
max_miles = 0

with open("taxi_1000.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        fare = float(row["Fare"])
        miles = float(row["Trip Miles"])

        total_fare += fare
        count += 1

        if miles > max_miles:
            max_miles = miles

average_fare = total_fare / count

print("Total fares:", total_fare)
print("Average fare:", average_fare)
print("Maximum trip miles:", max_miles)