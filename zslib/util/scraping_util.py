import requests
from requests.compat import urljoin
from selenium import webdriver
from lxml import html
import os, time

TIME_SLEEP = 1
driver = webdriver.Chrome


def get_html_obj(url, headers={}, sleep=TIME_SLEEP, encoding='auto'):
    response = requests.get(url, headers=headers)
    if encoding == 'auto':
        response.encoding = response.apparent_encoding
    elif encoding:
        response.encoding = encoding
    html_obj = html.fromstring(response.text)
    time.sleep(sleep)
    return html_obj


def get_html_obj_from_selenium(url, driver, sleep=TIME_SLEEP):
    """
    :param url:
    :param sleep:
    :param driver:
    :return:

    from scraping_util import driver
    dr = driver()
    html_obj = get_html_obj_from_selenium(url, 1, dr)
    dr.close()
    """
    driver.get(url)
    time.sleep(sleep)
    html_obj = html.fromstring(driver.page_source)
    return html_obj


def header_from_raw_string(head_str):
    head_lst = [l.split(':') for l in head_str.split('\n')]

    headers = {}
    for h in head_lst:
        headers[h[0]] = ''.join(h[1:]).strip()

    return headers


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