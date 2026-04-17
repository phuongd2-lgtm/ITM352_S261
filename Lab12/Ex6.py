import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
print("Opening URL:", url)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# get cleaner text pieces from the page
lines = list(soup.stripped_strings)

current_bank = ""

for line in lines:
    # save the current bank name
    if line in [
        "American Savings Bank",
        "Bank of Hawaii",
        "Central Pacific Bank",
        "Finance Factors",
        "First Hawaiian Bank",
        "Hawaii State Federal Credit Union",
        "Imperial Mortgage LLC",
        "Kama'aina Mortgage Group"
    ]:
        current_bank = line

    # print each mortgage-rate row
    elif "Fixed" in line or "ARM" in line:
        print(current_bank + " -> " + line)