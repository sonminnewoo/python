from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
# https://www.weather.go.kr/w/weather/forecast/mid-term.do

soup = BeautifulSoup(req.text, 'lxml')

# 1. 웹에서 필요한 데이터 가져온다

weather = {}
# dick 선언
for i in soup.find_all('location'):
    # 로케이션 태그 하위 항목들을 
    weather[i.find('city').text] = []
    for j in i.find_all('data') : 
        temp = []
        temp.append(j.find('tmef').text)
        temp.append(j.find('wf').text)
        temp.append(j.find('tmn').text)
        temp.append(j.find('tmx').text)
        weather[i.find('city').string].append(temp)

# print(weather)
# 데이터 베이스에 insert

import pymysql
con = pymysql.connect(host='127.0.0.1' , user='root', password='3123', 
                      db='pythondb' , charset='utf8')
cur = con.cursor()
# cur.execute("CREATE TABLE forcast(city VARCHAR(500),tmef VARCHAR(500),wf VARCHAR(500),tmn VARCHAR(500),tmx VARCHAR(500))")
# cur.execute("DROP TABLE forcast")
insert_sql = "insert into forecast(city, tmef, wf , tmn, tmx) values(%s,%s,%s,%s,%s)"

for i in weather :
    for j in weather[i] : 
        cur.execute(insert_sql,(i,j[0],j[1],j[2],j[3]))

con.commit()
con.close()