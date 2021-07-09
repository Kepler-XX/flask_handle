import requests
import json
import urllib.parse


def get(url):
    req = requests.get(url)
    return json.loads(req.text)


def post(url, post_data, headers):
    req = requests.post(url, post_data, headers)
    return json.loads(req.text)


def get_url_format(url, params=None):
    if params:
        if not isinstance(params, dict):
            raise Exception('params with a error format')
    if url:
        # url += '?' + '&'.join([str(key) + '=' + str(value) for key, value in params.items()])
        url = url + '?' + urllib.parse.urlencode(params)
    return url