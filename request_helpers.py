import requests


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
    request_url = 'https://stackoverflow.com/search?q=%s' % key_words_sting[1:]
    return request_url


def get_response(request):
    if is_url(request):
        response = requests.get(request).content
    else:
        request_url = create_request_url(request)
        response = requests.get(request_url).content
    return response