# https://www.weather.go.kr/w/obs-climate/land/city-obs.do
# 지역(이름) , 온도(현재기온) , 습도(습도)
# 강릉 1.8 97

import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
res = requests.get(URL)
soup = BeautifulSoup(res.content, 'html.parser')
txt = soup.select_one('#weather_table > tbody')


datas = []
for i in txt.select('tr') : 
    # txt 안에서 원하는 tr 테그만 가져온다 
    tds = i.select('td')
    datas.append([tds[0].text,tds[5].text,tds[-4].text])
    # temp = i.select_one('tr:nth-child(1) > td:nth-child(7)').text
    # humi = i.select_one('tr:nth-child(1) > td:nth-child(11)').text
print(datas)

# 안에 파일 넣기 

# weather.csv
import csv
with open('weather.csv','w', newline='', encoding='utf-8') as file:
    file.write('지역,기온,습도\n')
    for item in datas :
        row = ','.join(item)
        file.write(row+'\n')


# weather_pandas.csv
import pandas as pd
df_weather = pd.DataFrame(datas,columns = ('지역','기온','습도'))
df_weather.to_csv('weather_pandas.csv', encoding='utf=-8-sig',index=False)