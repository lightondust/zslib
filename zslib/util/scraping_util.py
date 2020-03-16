import requests
from selenium import webdriver
from lxml import html
import os, time

TIME_SLEEP = 1
driver = webdriver.Chrome


def get_driver(headless=False):
    if headless:
        from selenium.webdriver.chrome.options import Options

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1280,1024')

        dr = webdriver.Chrome('chromedriver', chrome_options=options)
        return dr
    else:
        dr = webdriver.Chrome()
        return dr


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
    html_obj = get_html_from_driver(driver)
    return html_obj


def get_html_from_driver(dr):
    html_obj = html.fromstring(dr.page_source)
    return html_obj


def header_from_raw_string(head_str):
    head_lst = [l.split(':') for l in head_str.split('\n')]

    headers = {}
    for h in head_lst:
        headers[h[0]] = ''.join(h[1:]).strip()

    return headers


def element_to_file(file_path, element):
    with open(file_path, 'w') as f:
        f.write(element_to_html_string(element))


def element_to_html_string(element):
    string = html.tostring(element, encoding='utf-8').decode()
    return string


def read_file(file_path):
    with open(file_path, 'r') as f:
        cont = f.read()
    return cont


def read_html(html_path):
    cont = read_file(html_path)
    html_obj_load = html.fromstring(cont)
    return html_obj_load


def download_file(url, file_path, headers={}, over_write=False):
    if over_write or (not os.path.exists(file_path)):
        r = requests.get(url, stream=True, headers=headers)
        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            time.sleep(TIME_SLEEP)
            return True
        else:
            print("code:{}, url:{}".format(r.status_code, url))
            return False