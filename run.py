import requests
from bs4 import BeautifulSoup

user_search_url = input()
try:
    request = requests.get(user_search_url)
except requests.exceptions.MissingSchema:
    print("Sorry")
    exit()

request_html = request.content
soup = BeautifulSoup(request_html, 'html.parser')


links = soup.find_all('div', 'result-link')

for link in links:
    print('https:%s' % link.a['href'])
