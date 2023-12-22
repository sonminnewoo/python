import requests
from bs4 import BeautifulSoup

header = {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/index.htm', headers=header)

soup = BeautifulSoup(req.content, 'html.parser')
# print(soup)
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
  datas.append([rank,title,singer,album])

print(datas)  

# 파일 melon.csv
import pandas as pd 
df = pd.DataFrame(datas, columns=('순위','제목','가수','앨범'))
df.to_csv('melon.csv',encoding='utf-8-sig',index=False)





