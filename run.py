import requests
from bs4 import BeautifulSoup


def is_url(request):
    try:
        requests.get(request)
    except requests.exceptions.MissingSchema:
        return False
    return True


def create_request_url(request):
    key_words = request.split()
    key_words_sting = ''
    for key_word in key_words:
        key_words_sting += '+%s' % key_word
    user_search = 'https://stackoverflow.com/search?q=%s' % key_words_sting[1:]
    return user_search

user_search = input()
if is_url(user_search):
    response = requests.get(user_search).content
else:
    user_search_url = create_request_url(user_search)
    response = requests.get(user_search_url).content

soup = BeautifulSoup(response, 'html.parser')
links = soup.find_all('div', 'result-link')
for link in links:
    print('https://stackoverflow.com%s' % link.a['href'])
