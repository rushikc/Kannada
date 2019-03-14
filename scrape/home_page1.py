from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
# import timeit
import time
import bs4
from bs4 import BeautifulSoup
from Kannada.kannada import letters as k
import  shelve


driver = webdriver.Chrome()  #open chrome webdriver.


driver.get("https://www.shabdkosh.com/kn/browse")


ele = driver.page_source #get page source html
src = BeautifulSoup(ele, 'lxml')

atag =  src.select('.abc')

l_links = []

home = 'https://www.shabdkosh.com'

for i in range(len(atag)):
    st = atag[i].text
    if st in k.klist:
        l_links.append(home + atag[i]['href'])


print(l_links)

db = shelve.open('link')
db['l_links'] = l_links
db.close()


# time.sleep(2)
driver.close()


