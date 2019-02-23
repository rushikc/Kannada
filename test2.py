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





for i in range(20):
    if(i%5 == 0):
        i=i+2
    print(i)

# driver = webdriver.Chrome()
# driver.get('https://www.shabdkosh.com/kn/translate/%E0%B2%85%E0%B2%95%E0%B3%8D%E0%B2%95%E0%B2%B0%E0%B3%86%E0%B2%AF/%E0%B2%85%E0%B2%95%E0%B3%8D%E0%B2%95%E0%B2%B0%E0%B3%86%E0%B2%AF-meaning-in-Kannada-English')
#
# ele = driver.page_source  # get page source html
# src = BeautifulSoup(ele, 'lxml')
# while True:
#     try:
#         time.sleep(1)
#         at = src.find_all('div', {'class': 'post'})
#         atag = at[0].find_all('a')
#
#         print(atag[2].text)
#
#     except Exception as e:
#         print(e)
#         driver.refresh()

