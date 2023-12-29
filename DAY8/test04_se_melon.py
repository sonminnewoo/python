from selenium import webdriver as wd
from selenium.webdriver.common.by import By

driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')
    # //*[@id="frm"]/div/table/tbody    /> 복사 하는것중 xpath 라는걸로 복사해준다
tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME , 'tr') # 1개일때는 find_element 여러개 일때는 find_elements 로 사용한다

datas = []
for tr in trs:
    rank = tr.find_element(By.CLASS_NAME, 'rank').text
    title = tr.find_element(By.CLASS_NAME, 'wrap_song_info').find_element(By.TAG_NAME,'a').text
    singer = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank02').find_element(By.TAG_NAME,'a').text   
    album = tr.find_element(By.CSS_SELECTOR, 'div.rank03').find_element(By.TAG_NAME, 'a').text
    like = tr.find_element(By.CLASS_NAME, 'cnt').text
    datas.append([rank,title,singer,album,like])

print(datas)

# melon_se.csv 파일로 내보내기 (순위, 제목, 가수, 앨범, 좋아요수)
import csv

csv_filename = 'melon_se.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # 헤더 쓰기
    csv_writer.writerow(['순위', '제목', '가수', '앨범', '좋아요 수'])
    
    # 데이터 쓰기
    for data in datas:
        csv_writer.writerow(data)

print(f'데이터가 {csv_filename} 파일로 저장되었습니다.')