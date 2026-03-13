import csv

total_fare = 0
count = 0
max_miles = 0

with open("taxi_1000.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        fare = float(row["Fare"])
        miles = float(row["Trip Miles"])

        if fare > 10:
            total_fare += fare
            count += 1

            if miles > max_miles:
                max_miles = miles

average_fare = total_fare / count

print("Total fares (over $10):", total_fare)
print("Average fare (over $10):", average_fare)
print("Maximum trip miles:", max_miles)