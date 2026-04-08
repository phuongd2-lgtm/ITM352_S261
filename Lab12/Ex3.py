#Parse the ITM Department website to find the people (faculty, grads, lecturers)
import urllib.request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


itm_url = "https://shidler.hawaii.edu/itm/people"

itm_html = urllib.request.urlopen(itm_url)
html_to_parse = BeautifulSoup(itm_html, "html.parser")  

print(html_to_parse.prettify())

# find and print just the name of the faculty memebers
list_of_faculty = html_to_parse.find_all("h2", class_="title")

itm_faculty = []
for faculty in list_of_faculty:
    itm_faculty.append(faculty.text.strip())
    print(faculty.text.strip())
