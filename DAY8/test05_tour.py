# https://www.hanatour.com/mma/smn/EX00000020
# 제주도 검색
# 호텔정보 검색

# 호텔명, 성급 , 금액 , 별점 

# 셀레니움 방식
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
# 본래 방식
import requests
from bs4 import BeautifulSoup
import time

url ='https://www.hanatour.com/all-search?page=1&tab=hotel&keyword=%EC%A0%9C%EC%A3%BC%EB%8F%84&pageSize=20'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')

driver = wd.Chrome()
driver.implicitly_wait(4)
driver.get('https://www.hanatour.com/mma/smn/EX00000020')

driver.find_element(By.ID, 'input_keyword').send_keys('제주도')
driver.find_element(By.CLASS_NAME, 'btn_search').click()
driver.find_element(By.CLASS_NAME, 'tabs').find_element(By.XPATH, '//*[@id="contents"]/div[2]/ul/li[3]').click()
# 주소 값을 들고 오게  하는것 
# pi 차트는 값을 어떻게 들고 올지 를 지정해줘야 한다 %.1f%% 으로

time.sleep(3)

selector = driver.find_elements(By.XPATH, '//*[@id="contents"]/div[3]/div[2]/div[2]/div[1]/ul/li/div/div[2]')
datas = []

for hotel_info in selector:
    hotelName = hotel_info.find_element(By.XPATH, 'div[1]/strong').text
    hotelStar = hotel_info.find_element(By.XPATH, 'div[2]/span[2]').text
    hotelCharge = hotel_info.find_element(By.XPATH, 'div[5]/div/div/strong').text
    hotelReview = hotel_info.find_element(By.XPATH, 'div[4]/strong').text
    datas.append([hotelName, hotelStar, hotelCharge, hotelReview])

print(datas)