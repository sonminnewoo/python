from bs4 import BeautifulSoup
import requests

req = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
soup = BeautifulSoup(req.text, 'html.parser')

#weather_table > tbody
tbody = soup.select_one('#weather_table > tbody')
# print(tbody)
datas =[]
for tr in tbody.select('tr'):
  tds = tr.select('td')
  datas.append([tds[0].text,tds[5].text,tds[-4].text])
  # print('지역 = ', tds[0].text)
  # print('기온 = ', tds[5].text)
  # print('습도 = ', tds[-4].text)
print(datas)  
# weather.csv
with open('weather.csv', 'w') as file:
  file.write('지역, 기온, 습도\n')
  for item in datas:
    row =','.join(item)
    file.write(row+'\n')


# weather_pandas.csv
import pandas as pd 
df_weather = pd.DataFrame(datas, columns = ('지역','기온','습도'))
df_weather.to_csv('weather_pandas.csv', encoding='utf-8-sig',
                  index=False)
    

