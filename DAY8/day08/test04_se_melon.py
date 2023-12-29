from selenium import webdriver as wd 
from selenium.webdriver.common.by import By

driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')
#   //*[@id="frm"]/div/table/tbody

tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

datas = []
for tr in trs:
  rank = tr.find_element(By.CLASS_NAME, 'rank').text
  title =tr.find_element(By.CLASS_NAME, 'wrap_song_info').find_element(By.TAG_NAME, 'a').text 
  #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02
  singer = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank02').find_element(By.TAG_NAME,'a').text
  #lst50 > td:nth-child(7) > div > div > div
  album = tr.find_element(By.CSS_SELECTOR, 'div.rank03').find_element(By.TAG_NAME,'a').text
  like = tr.find_element(By.CLASS_NAME, 'cnt').text
  datas.append([rank,title,singer,album,like])

print(datas)  
# melon_se.csv 파일로 내보내기 ('순위','제목','가수','앨범','좋아요 수')
import pandas as pd 
df1 = pd.DataFrame(datas, columns = ('순위','제목','가수','앨범','좋아요 수'))
df1.to_csv('melon_se.csv', encoding='utf-8-sig', index=False)


