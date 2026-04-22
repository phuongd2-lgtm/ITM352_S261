import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# load the JSON file
df = pd.read_json("Trips from area 8.json")

# drop missing values
df = df.dropna(subset=["fare", "trip_miles", "dropoff_community_area"])

# create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    df["fare"], 
    df["trip_miles"], 
    df["dropoff_community_area"]
)

# labels and title
ax.set_title("3D Plot of Fare, Trip Miles, and Dropoff Area")
ax.set_xlabel("Fare")
ax.set_ylabel("Trip Miles")
ax.set_zlabel("Dropoff Area")

plt.show()