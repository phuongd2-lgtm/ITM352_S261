#Get public license data from the city of Chicago's Data Portal

import pandas as pd
from sodapy import Socrata

# Create a Soadpy client to access the Chicago Data Portal
client = Socrata("data.cityofchicago.org", None)

# Specify the JSON file for license data 
json_file = "rr23-ymwb"

results = client.get(json_file, limit=500) 
# Convert the results to a DataFrame for easier analysis
df = pd.DataFrame.from_records(results)

#print(df.head())

vehicles_and_fuel_resources = df[("public_vehicle_number","vehicle_fuel_source")]
print("Public Vehicle Number and Fuel Source:")
print(vehicles_and_fuel_resources.head())

vehicles_by_fuel_source = vehicles_and_fuel_sources.groupby("Vehicle_fuel_source").count()
print(vehicles_by_fuel_source)
