import matplotlib.pyplot as plt
import numpy as np
import urllib
import bs4
import requests
# 위처럼 모듈 을 추가 해주는데 외부, 내부 라이브러리 를 추가한다        

# 'http://www.weather.go.kr/weather/observation/currentweather.jsp'
# 지역, 온도, 습도
# weather18.csv 로 저장

url = "http://www.weather.go.kr/weather/observation/currentweather.jsp"
# PageNumber = 1
finalpage = url
htmlObject = urllib.request.urlopen(finalpage)
webpage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webpage, 'html.parser')
tag = bsObject.select_one('#weather_table > tbody')

datas = []
for i in tag.select('tr') : 
    # txt 안에서 원하는 tr 테그만 가져온다 
    tds = i.select('td')
    # 거기서 td 만가져온다
    datas.append([tds[0].text,tds[5].text,tds[-4].text])
    # 그리고 거기서 필요한걸 append 로 위에서 만들었던 리스트에 넣어준다 원하는것만
    # tds[-4].text 은 뒤에서 4번째 를 의미 한다 
    
print(datas)

# 안에 파일 넣기 

# weather.csv
#  
import csv
with open('weather18.csv','w', newline='', encoding='utf-8') as file:
    file.write('지역,기온,습도\n')
    for item in datas :
        row = ','.join(item)
        file.write(row+'\n')


# weather_pandas.csv
# pandas 라이브러리 이용한 방식
    import pandas as pd
df_weather = pd.DataFrame(datas,columns = ('지역','기온','습도'))
df_weather.to_csv('weather_pandas18.csv', encoding='utf=-8-sig',index=False)