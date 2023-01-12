'''
함수는 이곳에 모아놓고 main.py를 간결히 할 방안 강구 
-> 클래스 활용 생각, 파이썬스러운 코딩 
'''

import selenium
import time
from db import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
URL = 'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=201&vSort=0&vtab=1'
#창업미디어 사이트 URL
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


def scroll():
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def pageToDB():
    info = driver.find_elements_by_css_selector('div.listMetaCol1 > ol') #사업체 상세내역
    lolist, typelist, sizelist = [], [], []
    for elem in info:
        elem = elem.text.splitlines()
        lolist.append(elem[0][9:])
        typelist.append(elem[1][12:])
        sizelist.append(elem[2][9:])
    # print(lolist)
    # print(typelist)
    # print(sizelist)

    id = driver.find_elements_by_css_selector('div.listMetaCol2 > h4 > span')    #사업체 id 리스트
    idlist = []
    for elem in id:    
        elem = int(elem.text)
        idlist.append(elem)
    # print(idlist)   


    money = driver.find_elements_by_css_selector('div.listMetaCol2 > ol')        #월수익예상, 초기자본
    expectlist, caplist = [], []
    for elem in money:
        elem = elem.text.splitlines()
        expectlist.append(elem[0][6:])
        caplist.append(elem[1][4:])
    # print(expectlist)
    # print(caplist)


    phoneNum = driver.find_elements_by_css_selector('.conPhone')                 #담당자 연락처
    phonelist = []
    for elem in phoneNum:    
        phonelist.append(elem.text[1:])
    # print(phonelist)   

    for a,b,c,d,e,f,g in zip(idlist,typelist,lolist,sizelist,expectlist,caplist,phonelist):
        print(a,b,c,d,e,f,g)
        cur.execute("INSERT INTO CHJP (id,foodType,locate,size,expectedMoney,capital,phoneNum) VALUES (%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g))
        conn.commit()
        
def collectAll():
    for n in range(1,20):
        time.sleep(1)
        scroll()
        pageToDB()
        page_bar = driver.find_elements_by_css_selector("div.paging > *")
        
        try:
            if n%10 != 0:
                page_bar[n%10].click()
            else:
                driver.find_element_by_xpath('//*[@id="contents"]/div[3]/div[1]/div/div[1]/span[2]/a').click()
        except:
            print("수집완료")
            break

    conn.commit()