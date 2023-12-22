import requests
from bs4 import BeautifulSoup

# 순위, 곡명, 가수, 앨범 출력

header = {'User-Agent' : 'Mozilla/5.0'}
res = requests.get('https://www.melon.com/chart/index.htm', headers=header)
soup = BeautifulSoup(res.content, 'html.parser')

tbody = soup.select_one('#frm > div > table > tbody')
trs = tbody.select('tr#lst50')

datas = []

for tr in trs :
    rank = tr.select_one('span.rank').string
    title = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
    singer = tr.select_one('div.ellipsis.rank02 > a').get_text()
    album = tr.select_one('div.rank03 > a').get_text()
    datas.append([rank, title, singer, album])
    print('순위 : ', rank)
    print('곡명 : ', title)
    print('가수 : ', singer)
    print('앨범 : ', album)

# 파일 melon.csv
import pandas as pd

df = pd.DataFrame(datas, columns=('순위', '제목', '가수', '앨범'))
df.to_csv('melon.csv', encoding='utf-8-sig', index=False)

