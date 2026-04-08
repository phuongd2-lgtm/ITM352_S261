# Grab 1 month interest rate data from the Treasury website
import ssl
import pandas as pd 
import urllib.request
import lxml

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202603"

# Open the URL and use read_html to read the data into a DataFrame
ssl._create_default_https_context = ssl._create_unverified_context

print("Opening url: " + url)
web_page = urllib.request.urlopen(url)
data_frame = pd.read_html(web_page)

#print(data_frame[0].info())
#print(data_frame[0]())

#Extract the 1 mont interest rate data
one_month_rate = data_frame[0].iloc[0,1]

#Interate through the data using intererows() and print the 1 month interest rate
for index, row in data_frame[0].iterrows():
    if row["Date"] == "2026-03-01":
        print("1 month interest rate on 2026-03-01: (one_month_rate) %")
        break