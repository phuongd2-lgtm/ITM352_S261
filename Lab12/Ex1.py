#Scrape data from the city of Chicago's Data Portal
#Print any line that has a <title> tag in it

import urllib.request
url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

print("Opening URL: " + url)
web_page = urllib.request.urlopen(url)

#Iterate through each line in the web page, searching for the <title> tag
for line in web_page:
    line = line.decode("utf-8") #Decode bytes to string
    if "<title>" in line: #Print the line with the tag, removing extra whitespace
        print(line.strip()) 