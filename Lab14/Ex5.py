import pandas as pd
import matplotlib.pyplot as plt

# load the JSON file
df = pd.read_json("Trips from area 8.json")

# drop missing values
df = df.dropna(subset=["fare", "trip_miles"])

# 1. scatter plot using plt.scatter()
plt.scatter(df["fare"], df["trip_miles"])
plt.title("Fare vs Trip Miles (scatter)")
plt.xlabel("Fare")
plt.ylabel("Trip Miles")
plt.show()

# 2. same plot using plt.plot()
plt.plot(df["fare"], df["trip_miles"], linestyle="none", marker=".")
plt.title("Fare vs Trip Miles (plot)")
plt.xlabel("Fare")
plt.ylabel("Trip Miles")
plt.show()

# 3. fancier version
plt.plot(df["fare"], df["trip_miles"], linestyle="none", marker="v", color="c", alpha=0.2)
plt.title("Fancy Fare vs Trip Miles")
plt.xlabel("Fare")
plt.ylabel("Trip Miles")
plt.show()