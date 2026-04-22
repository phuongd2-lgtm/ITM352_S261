import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the JSON file
df = pd.read_json("Trips from area 8.json")

# Drop rows with NA values in the relevant columns
df_clean = df.dropna(subset=['payment_type', 'tips'])

# Group by payment method and calculate the sum of tips
tip_sums = df_clean.groupby('payment_type')['tips'].sum()

# Create the plot
plt.figure(figsize=(10, 6))
tip_sums.plot(kind='bar', color='teal', edgecolor='black')

# Assign appropriate labels and a title
plt.title("Total Tips by Payment Method (Trips from Area 8)")
plt.xlabel("Payment Method")
plt.ylabel("Sum of Tips")

# Adjust layout for better visibility of labels
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot
plt.show()