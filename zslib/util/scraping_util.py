import requests
from requests.compat import urljoin
from lxml import html
import os, time

TIME_SLEEP = 1


def get_html_obj(url, headers={}, sleep=TIME_SLEEP, encoding='auto'):
    response = requests.get(url, headers=headers)
    if encoding == 'auto':
        response.encoding = response.apparent_encoding
    elif encoding:
        response.encoding = encoding
    html_obj = html.fromstring(response.text)
    time.sleep(sleep)
    return html_obj


def element_to_html_string(element):
    string = html.tostring(element, encoding='utf-8').decode()
    return string


def download_file(url, file_path, headers={}, over_write=False):
    if over_write or (not os.path.exists(file_path)):
        r = requests.get(url, stream=True, headers = headers)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            time.sleep(TIME_SLEEP)
            return True
        else:
            print("code:{}, url:{}".format(r.status_code, url))
            return False