import requests
from bs4 import BeautifulSoup

header = {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('http://www.melon.com/chart/index.htm',headers=header)
# 순위 제목 가수 앨범 python 스키마에 melon 테이블 추가
# 스키마 : MySQL 에서 OracleSQL 에서 테이블 개념 

import pymysql
import re

con = pymysql.connect(host='127.0.0.1' , user='root', password='3123', db='pythondb' , charset='utf8')
cur = con.cursor()
curss = con.cursor()

# 1. 멜론에서 정보 가져오기
soup = BeautifulSoup(req.content, 'html.parser')
txt = soup.select_one('#frm > div > table > tbody')
all_text = txt.findAll('tr')


trs = txt.select('tr#lst50')

datass = []
for tr in trs:

    #lst50 > td:nth-child(2) > div > span.rank
    rankss = tr.select_one('span.rank').get_text()
    
    titless = tr.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span').get_text()
    songnamess = tr.select_one('div.ellipsis.rank01 > span > a').get_text()
    singerss = tr.select_one('div.ellipsis.rank02 > a').get_text()
    albumss = tr.select_one('td:nth-child(7) > div > div > div > a').get_text()
    albumss = re.sub('\'','',albumss)
                    #  \' 는 \ 가 단지 ' (홑따음표만 지정하게 된다)
    print(datass)
    datass.append([rankss,titless,singerss,albumss])
    sql = "insert into melon value('"+rankss+"','"+titless+"','"+singerss+"','"+albumss+"')"
    curss.execute(sql)


con.commit()
con.close()


# def song(all_song):
#     rank = all_song.find('div' , {'class' : 'wrap t_center'}).text
#     # print(rank)
#     songName = all_song.find('div' , {'class' : 'ellipsis rank01'}).text.strip()
#     # print(songName.strip())
#     singerName = all_song.find('div' , {'class' : 'ellipsis rank02'}).text.strip()
#     # print(singerName)
#     albumName = all_song.find('div' , {'class' : 'ellipsis rank03'}).text.strip()
#     albumName = re.sub('\'','',albumName)
#     # print(albumName)
#     return [rank,songName,singerName[:18],albumName]

# song_list = []

# for i in all_text :
#     songs = song(i)
#     song_list.append(songs)
# print(song_list)

# # 2. 가져온 정보 MySQL 에 저장하기 



# # "insert into melon values('1','첫눈','')"

# for i in song_list : 
#     cur.execute("insert into userTable values('"+i[0]+"','"+i[1]+"', '"+i[2]+"', '"+i[3]+"')")

# con.commit()
# # 단위 실행
# con.close()
# # 반환  
