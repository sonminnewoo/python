from bs4 import BeautifulSoup
import requests

req = requests.get('http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
soup = BeautifulSoup(req.text, 'lxml')

insert_sql = "insert into forecast(city, tmef, wf, tmn, tmx) values(%s,%s,%s,%s,%s)"

weather={}
for i in soup.find_all('location'):
  weather[i.find('city').text] = []
  for j in i.find_all('data'):
    temp = []
    temp.append(j.find('tmef').text)
    temp.append(j.find('wf').text)
    temp.append(j.find('tmn').text)
    temp.append(j.find('tmx').text)
    weather[i.find('city').string].append(temp)

print(weather)  
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

import pymysql
con = pymysql.connect(host =dbURL , port = dbPort, user = dbUser, passwd = dbPass, db='pythondb', charset='utf8' )  
cur = con.cursor()
for i in weather:
  for j in weather[i]:
      cur.execute(insert_sql, (i, j[0],j[1],j[2],j[3]))
con.commit()  
con.close()


