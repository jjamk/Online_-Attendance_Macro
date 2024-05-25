# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# # 드라이버 초기화
# from selenium.webdriver.common.by import By


import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import pyautogui

chrome_options = webdriver.ChromeOptions()
# 브라우저 꺼짐방지 옵션
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
#s = Service('/Users/seohyeonkang/Desktop/roll/chromedriver')

#driver = webdriver.Chrome(service=s)

# URL 얻기
driver.get("https://lms.konyang.ac.kr/login/doLoginPage.dunet")

# 아이디/패스워드
user_id = '19615001'
user_pw = 'dkrlwhrqkf!55\n'

log_ID = driver.find_element(by=By.ID, value="id")
log_ID.click()
pyautogui.typewrite(user_id, interval=0.1)

log_PID = driver.find_element(by=By.ID, value="pass")
log_PID.click()
pyautogui.typewrite(user_pw, interval=0.3)

#log_BTN = driver.find_element(by=By.CLASS_NAME, value="btn_mormal_type")
# log_BTN.click()
time.sleep(1)

# 과목/주차/회차 입력
subject, week, num = input("과목/주차/회차/: ").split()

# lec_BTN = driver.find_element(by=By.ID, value="selfarea_202310UN0000031K01_01")
# lec_BTN.send_keys('\n')

# week번째 tr요소
# num번째 td요소

# 과목 찾기(ing)
s_search = driver.find_element(
    by=By.XPATH, value='//*[@id="selfarea_202310UN0000031K01_01"]/strong')

s_search_res = driver.find_element(
    by=By.XPATH,
    value='//*[@id="selfarea_202310UN0000031K01_01"]/strong').text
if s_search_res == subject:
    s_search.send_keys('\n')

print(s_search_res, subject, week, num)

# 오프라인출석 버튼클릭
lec_BTN2 = driver.find_element(
    by=By.XPATH, value='//*[@id="sidenav"]/nav/ul/div/ul/li[15]/a')
lec_BTN2.send_keys('\n')

# 해당하는 주차/차수 의 출석체크 버튼클릭
tmp = driver.find_elements(
    By.CSS_SELECTOR, value="#layout_content > div.sub_content > div > div > div.pg_row > div > table > tbody > tr")
tmp2 = len(tmp)
chasi = tmp2 / 15

num_xpath = '//*[@id="layout_content"]/div[1]/div/div/div[2]/div/table/tbody/tr[{0}]/td[5*{1}]/a'.format(
    int(week)*chasi-1, int(num))
n_search = driver.find_element(
    by=By.XPATH,
    value=num_xpath)
n_search.send_keys('\n')

# code_BTN = driver.find_element(
#     by=By.XPATH, value='//*[@id="layout_content"]/div[1]/div/div/div[2]/div/table/tbody/tr[19]/td[5]/a')
# code_BTN.send_keys('\n')

#pyautogui.typewrite(str(code), interval=0.1)
