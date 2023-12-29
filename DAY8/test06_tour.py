# https://tour.interpark.com/?mbn=tour

# 제주도 검색
# 국내숙소 더보기 
# 10개 페이지 전부 다 방문해서 

# 호텔명, 가격 

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

driver = wd.Chrome()
chrome_options = Options()
chrome_options.add_argument("--window-size=maxxmax")
driver.implicitly_wait(4)
driver.get('https://tour.interpark.com/?mbn=tour')

driver.find_element(By.CLASS_NAME, 'searchButton').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'searchForm').click()
time.sleep(1)
driver.find_element(By.ID, 'txtHeaderInput').send_keys('제주도')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'inputSearchBtn').click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'moreBtn').click()
selector = driver.find_elements(By.XPATH, '//*[@id="boxList"]/li[1]/div/div[2]')

time.sleep(1)
for pagehotell in selector : 
    name = pagehotell.find_element(By.XPATH, 'div[2]/div[1]/a').text
    print(name)

# driver.find_element(By.ID, 'input_keyword').send_keys('제주도')
# driver.find_element(By.CLASS_NAME, 'btn_search').click()
# driver.find_element(By.CLASS_NAME, 'tabs').find_element(By.XPATH, '//*[@id="contents"]/div[2]/ul/li[3]').click()
# # 주소 값을 들고 오게  하는것 
# # pi 차트는 값을 어떻게 들고 올지 를 지정해줘야 한다 %.1f%% 으로

# time.sleep(3)

# selector = driver.find_elements(By.XPATH, '//*[@id="contents"]/div[3]/div[2]/div[2]/div[1]/ul/li/div/div[2]')
# datas = []

# for hotel_info in selector:
#     hotelName = hotel_info.find_element(By.XPATH, 'div[1]/strong').text
#     hotelStar = hotel_info.find_element(By.XPATH, 'div[2]/span[2]').text
#     hotelCharge = hotel_info.find_element(By.XPATH, 'div[5]/div/div/strong').text
#     hotelReview = hotel_info.find_element(By.XPATH, 'div[4]/strong').text
#     datas.append([hotelName, hotelStar, hotelCharge, hotelReview])

# print(datas)