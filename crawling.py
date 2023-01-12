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

    pcname = driver.find_elements_by_css_selector('.listSubtitle')
    pcnamelist = []
    for elem in pcname:
        pcnamelist.append(elem.text)
        
    for a,b,c,d,e,f,g,h in zip(idlist,typelist,lolist,sizelist,expectlist,caplist,phonelist,pcnamelist):
        print(a,b,c,d,e,f,g)
        cur.execute("INSERT INTO chicken (id,foodType,locate,size,expectedMoney,capital,phoneNum,pcname) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(a,b,c,d,e,f,g,h))
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

urlList = {'커피':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=101&vSort=0&vtab=1',
           '빵':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=102&vSort=0&vtab=1',
           '아이스크림/도넛':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=104&vSort=0&vtab=1',
           '패스트푸드':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=106&vSort=0&vtab=1',
           '디저트/브런치/셀러드':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=111&vSort=0&vtab=1',
           '밥류':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=302&vSort=0&vtab=1',
           '중식':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=309&vSort=0&vtab=1',
           '퓨전':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=304&vSort=0&vtab=1',
           '고기':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=307&vSort=0&vtab=1',
           '고기2': 'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=311&vSort=0&vtab=1',
           '일식':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=308&vSort=0&vtab=1',
           '분식':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=310&vSort=0&vtab=1',
           '치킨':'http://www.changupmedia.com/cumedia/gage_list.asp?vKindCode=201&vSort=0&vtab=1'
           }

#여기에 창업미디어 사이트URL 도는 for문
URL = urlList['빵']
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(executable_path='chromedriver')   #드라이버 로드
driver.get(url=URL)                                         #해당 URL 브라우저로 

conn = connectDB()
cur = makeCursor(conn)
#여기에 테이블명에 변수를 넣을수 있으면 for문으로 가능
# cur.execute("DROP TABLE IF EXISTS bake")
cur.execute("""CREATE TABLE test (
				id int NOT NULL,
                foodType VARCHAR(32),
                locate VARCHAR(32),
                size VARCHAR(32),
                expectedMoney VARCHAR(32),
                capital VARCHAR(32),
				phoneNum VARCHAR(32),
                pcname VARCHAR(64));
			""")

collectAll()

driver.close()

