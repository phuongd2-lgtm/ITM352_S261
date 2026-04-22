import pandas as pd
import matplotlib.pyplot as plt

# load the JSON file
df = pd.read_json("Trips from area 8.json")

# drop missing values (important)
df = df.dropna(subset=["trip_miles"])

# create histogram
plt.hist(df["trip_miles"], bins=20)

# labels and title
plt.title("Histogram of Trip Miles")
plt.xlabel("Trip Miles")
plt.ylabel("Frequency")

# show plot
plt.show()