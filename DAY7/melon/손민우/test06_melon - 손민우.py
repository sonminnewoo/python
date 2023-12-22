
# http://www.melon.com/chart/index.htm
#  위에서순위, 곡명, 가수, 앨범, ==> 출력

import requests
from bs4 import BeautifulSoup

header = { 'User-Agent' : 'Mozilla/5.0'}
req = requests.get('http://www.melon.com/chart/index.htm',headers=header)

soup = BeautifulSoup(req.content, 'html.parser')
txt = soup.select_one('#frm > div > table > tbody')
all_text = txt.findAll('tr')


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

song_list = []

for i in all_text :    
    songs = song(i)
    song_list.append(songs)
print(song_list)
