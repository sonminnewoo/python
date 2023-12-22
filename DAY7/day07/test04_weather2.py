from bs4 import BeautifulSoup
import requests
import pymysql

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

con = pymysql.connect(host =dbURL , port = dbPort, user = dbUser, passwd = dbPass, db='pythondb', charset='utf8' )  
cur = con.cursor()

req = requests.get('http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
soup = BeautifulSoup(req.text, 'lxml')

insert_sql = "insert into forecast2(city, tmef, wf, tmn, tmx) values(%s,%s,%s,%s,%s)"

select_sql = "select tmef from forecast2 order by tmef desc limit 1"
cur.execute(select_sql)
last_data = cur.fetchone() # 최신날짜
print(last_data)
print(type(last_data))
for i in soup.find_all('location'):
  city = i.find('city').text
  for j in i.find_all('data'):
    #맨 처음 데이터이거나        last_data 보다 최신날짜
    if (last_data is None) or(last_data[0] <  j.find('tmef').text) :  
      tmef = j.find('tmef').text
      wf = j.find('wf').text
      tmn = j.find('tmn').text
      tmx =j.find('tmx').text
      cur.execute(insert_sql, (city, tmef,wf,tmn,tmx))
con.commit()  
con.close()


