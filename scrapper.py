import requests
from bs4 import BeautifulSoup


indeed_result = requests.get("https://www.indeed.com/jobs?q=python")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')

pages = []

for link in links[:-1]:
    # pages.append(link.find("span").string)
    # pages.append(link.string)
    # a안에 span 요소 하나만 있어서 가능
    pages.append(int(link.string))

# pages = pages[:-1]
max_page = pages[-1]

for n in range(max_page):
    print(f"start={n*50}")

# print(max_page)
# print(pages)
# print(pagination)
# print(indeed_soup)
# print(indeed_result.text)

# https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch
