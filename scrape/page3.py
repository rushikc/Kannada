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

co = webdriver.ChromeOptions()
co.add_argument("log-level=3")
co.add_argument("--headless")


def get_proxies(co=co):
    driver = webdriver.Chrome(chrome_options=co)
    driver.get("https://free-proxy-list.net/")

    PROXIES = []
    proxies = driver.find_elements_by_css_selector("tr[role='row']")
    for p in proxies:
        result = p.text.split(" ")

        if result[-1] == "yes":
            PROXIES.append(result[0] + ":" + result[1])

    driver.close()
    return PROXIES


ALL_PROXIES = get_proxies()

print(ALL_PROXIES)
print(len(ALL_PROXIES))
# exit()


def proxy_driver(PROXIES, co=co):
    prox = Proxy()

    if PROXIES:
        pxy = PROXIES[-1]
    else:
        print("--- Proxies used up (%s)" % len(PROXIES))
        PROXIES = get_proxies()

    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = pxy
    prox.socks_proxy = pxy
    prox.ssl_proxy = pxy

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(chrome_options=co, desired_capabilities=capabilities)

    return driver


# --- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
driver = proxy_driver(ALL_PROXIES)

# options = Options()
# options.add_argument('--proxy-server=46.102.106.37:13228')
# driver = webdriver.Firefox() #open chrome webdriver.
db = shelve.open('dict')
num  = db['num2']
db.close()


import random
while num < len(txt):

    try:
        delay = random.randint(1,5)
        print('sleep start ',delay)
        time.sleep(delay)
        print('sleep stop')
        l=num

        # if(flag == 0):
        #     i = input()
        #     flag = 1

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
            db['num2'] = num
            print(db[str(l)])
            db.close()
            driver = proxy_driver(ALL_PROXIES)   #change driver with different proxy

            continue

        print(l)

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
            db['num2'] = l
            print(db[str(l)])
            db.close()
        else:
            db[str(l)] = ['em']
            db['num2']  = l
            db.close()
        num=num+1


    except:
        print('outer exc')
        continue
    finally:
        db = shelve.open('dict')
        db['num2'] = l
        db.close()


driver.close()