# Create a dataframe from individual lists,
#Do some simple statistics on the data. 

import pandas as pd

#List of individual ages
ages = [25, 30, 35, 40, 45, 50, 18, 60, 65]

#List of individual names and genders
names =["John", "Jane", "Doe", "Smith", "Emily", "Michael", "Sarah", "David", "Laura"]
gender = ["m", "f", "m", "m", "f", "m", "f", "m", "f"]

# Create a dictionary from the lists of ages and genders
dict = zip(ages, gender)
#print(list(dict))

# Create a dataframe from the dictionary
df = pd.DataFrame(dict,index=names,columns=["ages", "genders"])
print(df)

summary = df.describe()
print(summary)

# Calculate average age by gender
average_age_by_gender = df.groupby("genders")["ages"].mean()
print("\nAverage age by gender: \n", average_age_by_gender)