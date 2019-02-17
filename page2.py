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


db = shelve.open('link')
l_links = db['l_links']
db.close()

home = 'https://www.shabdkosh.com'
print(l_links)
print(len(l_links))
l3_links = []
l2_links = []
for i in range(len(l_links)):

    driver.get(l_links[i])
    time.sleep(1)
    ele = driver.page_source  # get page source html
    src = BeautifulSoup(ele, 'lxml')

    atag = src.find_all('a')

    for tag in atag:
        st1 = tag
        st1 = str(st1['href'])
        if(st1.__contains__(k.klist[i] + '/') and st1.__contains__('browse')):
            l2_links.append(home + st1)


    print(l2_links)

    for link2 in l2_links:
        driver.get(link2)
        ele2 = driver.page_source  # get page source html
        src2 = BeautifulSoup(ele2, 'lxml')

        atag2 = src.find_all('a')

        # print(atag2)

        for link3 in atag2:
            st3 = link3['href']
            st3 = str(st3)

            if st3.__contains__('translate/') and st3.__contains__('meaning'):
                l3_links.append(home + st3)


        print(l3_links)

        # driver.close()
        # exit()



db = shelve.open('link.db')
db['l3_links'] = l3_links
db.close()
driver.close()
exit()