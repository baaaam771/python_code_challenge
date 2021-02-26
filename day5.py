import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")

table = soup.find("table", {"class": "table"})

# tbody = table.find_all('tbody')
tbody = table.find("tbody")

# print(tbody)
tr = tbody.find_all('tr')

# print(tr)

# for a in tr:
#   td = tbody.find_all('td')


td = tbody.find_all('td')

for a in td:
    print(a.string)

# pages =[]

# for link in links[:-1]:
#   # pages.append(link.find("span").string)
#   # pages.append(link.string)
#   # a안에 span 요소 하나만 있어서 가능
#   pages.append(int(link.string))

# # pages = pages[:-1]
# max_page = pages[-1]
