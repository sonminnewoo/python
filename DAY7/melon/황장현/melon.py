import requests
from bs4 import BeautifulSoup
import pandas as pd

# https://www.melon.com/chart/index.htm
# 순위 곡명 가수 앨범을 추출하여 출력

header = {'User-Agent' : 'Mozilla/5.0'} # user-agent 설정
req = requests.get('https://www.melon.com/chart/index.htm',headers=header)
bs = BeautifulSoup(req.content,'html.parser')

tbody = bs.select_one('#frm > div > table > tbody')
tr=tbody.select('tr')
sList=[]
for i in tr :
    rank = i.select_one('td > div > span.rank').string
    song = i.select_one('div.ellipsis.rank01 > span > a').string
    singer = i.select_one('div.ellipsis.rank02 > a').string
    album = i.select_one('td:nth-child(7) > div > div > div > a').string
    sList.append([rank,song,singer,album])

df_sList = pd.DataFrame(sList,columns=['순위','곡명','가수','앨범'])
df_sList.to_csv("melon.csv",encoding='utf-8-sig',index=False)
print("파일 생성 완료")