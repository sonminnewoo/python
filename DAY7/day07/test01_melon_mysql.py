import requests
from bs4 import BeautifulSoup
import pymysql
import re

# db셋팅
con = pymysql.connect(host = '127.0.0.1', user='root', password=
                      '1234', db='pythondb', charset='utf8')
cur = con.cursor()

header = {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/index.htm', headers=header)

soup = BeautifulSoup(req.content, 'html.parser')
tbody = soup.select_one('#frm > div > table > tbody')
#lst50
trs = tbody.select('tr#lst50')

datas = []
# 순위 제목 가수 앨범
for tr in trs:
  rank = tr.select_one('span.rank').string
  #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
  title = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
  singer = tr.select_one('div.ellipsis.rank02 > a').get_text()
  album = tr.select_one('div.rank03 > a').get_text()
  album = re.sub('\'','',album)
  # 순위 제목 가수 앨범 pythondb  스키마에 melon 테이블에 추가
  # sql = "insert into melon values('1','첫눈','EXO','겨울')"
  sql = "insert into melon values('"+rank+"','"+title+"','"+singer+"','"+album+"')"
  cur.execute(sql)
  datas.append([rank,title,singer,album])
  # print(datas) 

con.commit()
con.close()    