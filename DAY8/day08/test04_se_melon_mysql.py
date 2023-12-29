from selenium import webdriver as wd 
from selenium.webdriver.common.by import By
import pymysql
import re

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
con = pymysql.connect(host = dbURL, port=dbPort, user = dbUser, password=dbPass,
                      db='pythondb', charset='utf8')

cur = con.cursor()
insert_sql="insert into melon_se(ranks, subject,singer, album, likes) values(%s,%s,%s,%s,%s)"
###########
driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')
#   //*[@id="frm"]/div/table/tbody

tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

for tr in trs:
  ranks = tr.find_element(By.CLASS_NAME, 'rank').text
  title =tr.find_element(By.CLASS_NAME, 'wrap_song_info').find_element(By.TAG_NAME, 'a').text 

  singer = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank02').find_element(By.TAG_NAME,'a').text

  album = tr.find_element(By.CSS_SELECTOR, 'div.rank03').find_element(By.TAG_NAME,'a').text
  likes = tr.find_element(By.CLASS_NAME, 'cnt').text
  likes = int(re.sub(',','', likes))

  cur.execute(insert_sql,(ranks,title,singer,album,likes))
print("저장완료")
con.commit()
con.close()  




