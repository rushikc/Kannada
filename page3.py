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




db = shelve.open('link')
txt = db['l3_links']
db.close()

print(txt[30])

l='https://www.shabdkosh.com/kn/translate/%E0%B2%85%E0%B2%82%E0%B2%95/%E0%B2%85%E0%B2%82%E0%B2%95-meaning-in-Kannada-English'
driver = webdriver.Chrome()  #open chrome webdriver.
driver.get(l)

ele = driver.page_source  # get page source html
src = BeautifulSoup(ele, 'lxml')
at = src.find_all('div',{'class':'col-sm-12'})
atag = at[0].find_all('a')


s1 = str(at[0].h3.text).upper()


words = []
if(s1.__contains__('VERB')):
    words.append('verb')
if(s1.__contains__('NOUN')):
    words.append('noun')
if(s1.__contains__('ADJECTIVE')):
    words.append('adjective')

for st in atag:
    st1 = st.text
    st1 =str(st1)
    words.append(st1)


print(words)

at2 = src.find_all('div',{'class':'col-lg-4 col-md-5'})
h3 = at2[0].find_all('h3')

name = []

for i in h3:
   st1 = str(i.text)
   st1 = st1.replace('\xa0','')
   name.append(st1)

tb = at2[0].find_all('table')

for k in range(len(tb)):
    at3 = tb[k].find_all('a')
    words.append(name[k])
    for tag in at3:
        st3 = str(tag.text)
        words.append(st3)


print(words)
driver.close()