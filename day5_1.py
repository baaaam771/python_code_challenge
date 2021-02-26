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

td_countrys = tbody.select("td:nth-of-type(4n+1)")
td_codes = tbody.select("td:nth-of-type(4n+3)")
countrys = []
codes = []

for a in td_countrys:
    countrys.append(a.string)

for b in td_codes:
    codes.append(b.string)


# print(countrys)
# print(codes)
# print(td_countrys)
# print(countrys)
# print(tbody)

dictionary = {}


for country, code in zip(countrys, codes):
    if codes == None:
        pass
    else:
        # print(country, code)
        dictionary[country.capitalize()] = code

# print(dictionary)

all_countrys = dictionary.keys()

# print(all_countrys)
index_dict = {}
print("Hello Please choose select a country by number")
for i, v in enumerate(all_countrys):
    print("# {} {}".format(i, v))
    index_dict[i] = v

# print(index_dict)


def test():

    try:
        n = int(input("#: "))
        if n not in index_dict:
            print("Choose a number from the list")
            test()
        elif n in index_dict:
            num = int(n)
            ans = dictionary[index_dict[num]]
            print("You choose", index_dict[num])
            print("The currency code is", ans)
    except:
        print("That wasn't a number")
        test()


test()
