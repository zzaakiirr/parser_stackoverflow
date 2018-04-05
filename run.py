from bs4 import BeautifulSoup

import request_helpers

entered_question = input()
response = request_helpers.get_response(entered_question)

soup = BeautifulSoup(response, 'html.parser')
links = soup.find_all('div', 'result-link')
for link in links:
    print('https://stackoverflow.com%s' % link.a['href'])
