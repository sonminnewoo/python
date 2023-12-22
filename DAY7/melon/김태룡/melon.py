import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

##
## #lst50 > td:nth-child(8) > div > button > span.cnt > span  : 좋아요 수
##

header = {'User-Agent' : 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/index.htm'
page = requests.get(url,headers=header)
soup = bs(page.text , 'html.parser')


rank = soup.select('#lst50 > td:nth-child(2) > div > span.rank')
title = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
musician = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
album = soup.select('#lst50 > td:nth-child(7) > div > div > div > a')

lst = []
for r,t,m,a in zip(rank,title,musician,album):
    print(r.text,'위 / ' , t.text,' / ', m.text, ' / ',a.text)
    lst.append([r.text,t.text,m.text,a.text])
    
df = pd.DataFrame(lst, columns=('순위','제목','가수','앨범명'))
df.to_csv('melon.csv', encoding ='utf-8-sig',index=False)
print('출력완료')

