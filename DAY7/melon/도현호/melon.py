import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0'}
req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
soup = BeautifulSoup(req.content, 'html.parser')

all_songs = soup.select('div#wrap div div span a')
name = []
song = []
rank = 2
for i in all_songs:
    ob=i.text
    if rank == 202:
        break
    if rank % 2 == 0:
        name.append(ob)
        print(int(rank / 2), ob, end=' | ')
    else:
        song.append(ob)
        print(ob)
    rank += 1

df = pd.DataFrame({'Rank': list(range(1, 101)),  'Song': name, 'Artist': song})

df.to_csv('song.csv', encoding='utf-8-sig', index=False)
