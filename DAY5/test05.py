# https://www.weather.go.kr/w/obs-climate/land/city-obs.do
# 지역(이름) , 온도(현재기온) , 습도(습도)
# 강릉 1.8 97

import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
# url 지정
res = requests.get(URL)
# url 읽기
soup = BeautifulSoup(res.content, 'html.parser')
# url parcer . 파싱 ! 테그형식으로 변경
txt = soup.select_one('#weather_table > tbody')
# 원하는 클단위 지정 

datas = []
for i in txt.select('tr') : 
    # txt 안에서 원하는 tr 테그만 가져온다 
    tds = i.select('td')
    datas.append([tds[0].text,tds[5].text,tds[-4].text])
    
print(datas)

# 안에 파일 넣기 

# weather.csv
# csv 라이브러리 이용한 방식
import csv
with open('weather.csv','w', newline='', encoding='utf-8') as file:
    file.write('지역,기온,습도\n')
    for item in datas :
        row = ','.join(item)
        file.write(row+'\n')


# weather_pandas.csv
# pandas 라이브러리 이용한 방식
import pandas as pd
df_weather = pd.DataFrame(datas,columns = ('지역','기온','습도'))
df_weather.to_csv('weather_pandas.csv', encoding='utf=-8-sig',index=False)