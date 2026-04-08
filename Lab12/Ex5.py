#Get a JSON file from the city of Chicago's Data Portal and analyze the driver type

import pandas as pd
import requests

#Create a REST query to get the JSON data for driver types

search_results = requests.get("https://data.cityofchicago.org/resource/ijzp-q8t2.json?$select=driver_type,count(*)&$group=driver_type") 

results_json = search_results.json()
print("Driver types and their counts:")
print(results_json)

#Convert the JSON results to a DataFrame for easier analysis
results_df = pd.DataFrame(results_json)
results_df.columns = ["Driver Type", "Count"]
results_df = results_df.sort_index("driver_type")

print("\nDriver types and their counts (DataFrame):")
print(results_df)