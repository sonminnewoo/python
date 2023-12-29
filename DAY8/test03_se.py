from selenium import webdriver as wd
from selenium.webdriver.common.by import By
driver = wd.Chrome()
driver.implicitly_wait(4)
driver.get('https://naver.com')

# 크롬 버전과 크롬 드라이브를 일치시키고 코드 폴더에 드라이버 를 넣어주고
# 이렇게 연결되면 
driver.find_element(By.ID, 'query').send_keys('파이썬')
# 검색창 의 태그의 id 가 query 로 되어있고 find_element 로 찾고 그것에 send_keys 으로 파이썬 을 입력한다

driver.find_element(By.CLASS_NAME, 'btn_search').click()
#CLASS_NAME 검색 아이콘 의 태그이고 ID 가 btn_search 이고 그것을 . click() 한다
