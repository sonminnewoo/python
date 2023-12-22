from bs4 import BeautifulSoup
import requests

header ={'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/index.htm', headers= header)
soup = BeautifulSoup(req.content, 'html.parser')
tbody = soup.select_one('#frm>div>table>tbody')
trs = tbody.select('tr#lst50')
# span.rank = 순위
# div.ellipsis rank01>span>a = 곡명
# div.ellipsis rank02>a = 가수명
# div.ellipsis rank03>a = 앨범명

chart = []
# 순위 제목 가수 앨범
for tr in trs:
    rank = tr.select_one('span.rank').string
    title = tr.select_one('div.ellipsis.rank01>span>a').string
    singer = tr.select_one('div.ellipsis.rank02>a').string
    album = tr.select_one('div.ellipsis.rank03>a').string
    chart.append([rank, title, singer, album])
print(chart)

# 파일 melon.csv
import pandas as pd
df = pd.DataFrame(chart, columns = ('순위', '곡명', '가수명', '앨범'))
df.to_csv('melon.csv', encoding='utf-8-sig', index=False)