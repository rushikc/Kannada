from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
# import timeit

import selenium
import time
import bs4
from bs4 import BeautifulSoup
from Kannada.kannada import letters as k
import shelve


# driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
from selenium import webdriver
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

import time

name = []
words = []
# print(l)

html = open('1.html','r')
ele = BeautifulSoup(html, 'html.parser')

# ele = driver.page_source  # get page source html
src = BeautifulSoup(ele, 'lxml')

try:
    try:
        at = src.find_all('div', {'class': 'col-sm-12'})
        atag = at[0].find_all('a')
        s1 = str(at[0].h3.text).upper()
        at2 = src.find_all('div', {'class': 'col-lg-4 col-md-5'})
    except:
        at = src.find_all('div', {'class': 'col-sm-4'})
        atag = at[0].find_all('a')
        s1 = str(at[0].h3.text).upper()
        at2 = src.find_all('div', {'class': 'col-lg-4 col-md-4'})

    if (s1.__contains__('VERB')):
        words.append(2)
    if (s1.__contains__('NOUN')):
        words.append(1)
    if (s1.__contains__('ADJECTIVE')):
        words.append(3)
    if (s1.__contains__('ADVERB')):
        words.append(4)

    for st in atag:
        st1 = st.text
        st1 = str(st1)
        words.append(st1)

    try:
        h3 = at2[0].find_all('h3')
    except:
        print('inner exc')





    for i in h3:
        st1 = str(i.text).upper()
        st1 = st1.replace('\xa0', '')
        if (st1.__contains__('VERB')):
            name.append(2)
        if (st1.__contains__('NOUN')):
            name.append(1)
        if (st1.__contains__('ADJECTIVE')):
            name.append(3)
        if (st1.__contains__('ADVERB')):
            words.append(4)

    tb = at2[0].find_all('table')

    for k in range(len(tb)):
        at3 = tb[k].find_all('a')
        words.append(name[k])
        for tag in at3:
            st3 = str(tag.text)
            words.append(st3)



except:
    print('outer exc')

