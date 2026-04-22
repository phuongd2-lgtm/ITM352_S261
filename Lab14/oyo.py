import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load CSV file
df = pd.read_csv("taxi trips Fri 7_7_2017.csv")

# drop missing values
df = df.dropna(subset=["pickup_community_area", "dropoff_community_area"])

# create matrix (counts of trips)
heatmap_data = pd.crosstab(
    df["pickup_community_area"], 
    df["dropoff_community_area"]
)

# plot heatmap
sns.heatmap(heatmap_data)

# labels and title
plt.title("Heatmap of Pickup vs Dropoff Areas")
plt.xlabel("Dropoff Community Area")
plt.ylabel("Pickup Community Area")

plt.show()