import pandas as pd
import matplotlib.pyplot as plt

# load the JSON file
df = pd.read_json("Trips_Fri07072017T4 trip_miles gt1.json")

# drop missing values
df = df.dropna(subset=["fare", "tips"])

# create scatter plot
plt.scatter(df["fare"], df["tips"])

# labels and title
plt.title("Fare vs Tips")
plt.xlabel("Fare")
plt.ylabel("Tips")

plt.show()