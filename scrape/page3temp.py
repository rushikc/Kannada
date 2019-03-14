
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

db = shelve.open('link')
txt = db['l3_links']
db.close()
# driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
from selenium import webdriver
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

import time

#install anonymox proxy extension into below drivers manually after opening drive and set different proxy for each driver
driver1 = webdriver.Chrome()  #open chrome webdriver.
driver2 = webdriver.Chrome()  #open chrome webdriver.
driver3 = webdriver.Chrome()  #open chrome webdriver.
driver4 = webdriver.Chrome()  #open chrome webdriver.
driver5 = webdriver.Chrome()  #open chrome webdriver.
driver6 = webdriver.Chrome()  #open chrome webdriver.
driver7 = webdriver.Chrome()  #open chrome webdriver.

driver = driver1

def rotate_proxy():
    dr = [driver1,driver2,driver3,driver4,driver5,driver6,driver7]

    db = shelve.open('dict')
    cur_n = db['d']
    db['d'] = (cur_n+1)%len(dr)
    db.close()

    cur_n+=1
    cur_n = cur_n % len(dr)

    driver_t = dr[cur_n]

    return driver_t




db = shelve.open('dict')
num  = db['num']
db.close()
print(num)

flag = 0
driver.set_page_load_timeout(360000)
driver.implicitly_wait(360000)

import random
while num < len(txt):

    try:
        delay = random.randint(1, 5)
        print('sleep start ', delay)
        time.sleep(delay)
        print('sleep stop')
        l=num
        print(l)
        if(flag == 0):
            i = input()
            flag = 1

        name = []
        words = []
        # print(l)

        driver.get(txt[l])

        ele = driver.page_source  # get page source html
        src = BeautifulSoup(ele, 'lxml')


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

            num+=1
            db = shelve.open('dict')
            db[str(l)] = ['not']
            db['num'] = num
            print(db[str(l)])
            db.close()
            driver = rotate_proxy()   #change driver with different proxy

            continue



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

        db = shelve.open('dict')

        if len(words) > 0:
            # print(words)
            db[str(l)] = words
            db['num'] = l
            print(db[str(l)])
            db.close()
        else:
            db[str(l)] = ['em']
            db['num']  = l
            db.close()
        num=num+1


    except:
        print('outer exc')
        continue
    finally:
        db = shelve.open('dict')
        db['num'] = l
        db.close()


driver.close()