
# http://www.melon.com/chart/index.htm
#  위에서순위, 곡명, 가수, 앨범, ==> 출력
# 좋아요 는 제외하는것은 총건수 에서 좋아요 수는 정적으로
# 표시 하지않는다, 동적으로 표시한다는 얘기  

import requests
from bs4 import BeautifulSoup

header = { 'User-Agent' : 'Mozilla/5.0'}
req = requests.get('http://www.melon.com/chart/index.htm',headers=header)

# url = 'http://www.melon.com/chart/index.htm'
# htmlObject = urllib.requests.urlopen(url)
# webPage = htmlObject.read()
# bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

soup = BeautifulSoup(req.content, 'html.parser')
# print(soup)
txt = soup.select_one('#frm > div > table > tbody')
all_text = txt.findAll('tr')
# 위를 셀렉트 로 표현한다면 all_text = txt.select('tr#lst50') 이런식 으로 할수있다


def song(all_song):
    rank = all_song.find('div' , {'class' : 'wrap t_center'}).text
    # print(rank)
    songName = all_song.find('div' , {'class' : 'ellipsis rank01'}).text.strip()
    # print(songName.strip())
    singerName = all_song.find('div' , {'class' : 'ellipsis rank02'}).text.strip()
    # print(singerName)
    albumName = all_song.find('div' , {'class' : 'ellipsis rank03'}).text.strip()
    # print(albumName)
    return [rank,songName,singerName[:18],albumName]

# all_song 라는걸로 지정을 해야하는데 저 song 안의 메소드에서는 txt 위치를 지정하다보니 
# 문제가 발생 했었다

song_list = []
# songs = song(txt)
# print(songs)
for i in all_text :    
    songs = song(i)
    song_list.append(songs)
print(song_list)

################################ 선생님 하신거 
# from bs4 import BeautifulSoup
# import requests

# header ={'User-Agent' : 'Mozilla/5.0'}
# req = requests.get('https://www.melon.com/chart/index.htm', headers= header)
# soup = BeautifulSoup(req.content, 'html.parser')
# tbody = soup.select_one('#frm>div>table>tbody')
# trs = tbody.select('tr#lst50')
# # span.rank = 순위
# # div.ellipsis rank01>span>a = 곡명
# # div.ellipsis rank02>a = 가수명
# # div.ellipsis rank03>a = 앨범명

# chart = []
# # 순위 제목 가수 앨범
# for tr in trs:
#     rank = tr.select_one('span.rank').string
#     title = tr.select_one('div.ellipsis.rank01>span>a').string
#     singer = tr.select_one('div.ellipsis.rank02>a').string
#     album = tr.select_one('div.ellipsis.rank03>a').string
#     chart.append([rank, title, singer, album])
# print(chart)

# # 파일 melon.csv
# import pandas as pd
# df = pd.DataFrame(chart, columns = ('순위', '곡명', '가수명', '앨범'))
# df.to_csv('melon.csv', encoding='utf-8-sig', index=False)