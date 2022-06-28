import requests 
from bs4 import BeautifulSoup
# import pprint

# page = requests.get('https://www.target.com/c/formula-nursing-feeding-baby/-/N-5xtkh?lnk=snav_rd_formula')
page = requests.get('https://github.com/trending')
print(page)


soup = BeautifulSoup(page.text, 'html.parser')
repo = soup.find(class_="repo-list")
repo_list = repo.find_all(class_='col-12 d-block width-full py-4 border-bottom')
print(len(repo_list))

# print(soup)

# products = soup.find(class_="Link__StyledLink-sc-4b9qcv-0")
# print(products)
# print(len(products))