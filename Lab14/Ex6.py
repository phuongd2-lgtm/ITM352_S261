import pandas as pd
import matplotlib.pyplot as plt

# load the JSON file
df = pd.read_json("Trips from area 8.json")

# drop missing values
df = df.dropna(subset=["fare", "trip_miles"])

# filter out 0-mile trips
df = df[df["trip_miles"] > 0]

# filter out trips less than 2 miles
df = df[df["trip_miles"] >= 2]

# create scatter plot
plt.scatter(df["fare"], df["trip_miles"])

# labels and title
plt.title("Fare vs Trip Miles (Trips >= 2 miles)")
plt.xlabel("Fare")
plt.ylabel("Trip Miles")

# save the plot
plt.savefig("FaresXmiles.png")

plt.show()