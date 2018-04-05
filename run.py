import requests
from bs4 import BeautifulSoup


user_search_url = input()
try:
    response = requests.get(user_search_url).content
except requests.exceptions.MissingSchema:
    print("Sorry, you entered wrong url")
    exit()
soup = BeautifulSoup(request_html, 'html.parser')
links = soup.find_all('div', 'result-link')
for link in links:
    print('https:%s' % link.a['href'])
