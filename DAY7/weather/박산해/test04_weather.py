from bs4 import BeautifulSoup
import requests
import pymysql
import re

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "root"

con = pymysql.connect(host =dbURL , port = dbPort, user = dbUser, passwd = dbPass, db='pythondb', charset='utf8' )
req = requests.get('http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stanId=108')
soup = BeautifulSoup(req.text, 'lxml')

ols = soup.find('body')
infos = ols.find_all('location')

insert_sql = "insert into forecast(city, tmef, wf, tmn, tmx) values(%s,%s,%s,%s,%s)"

cur = con.cursor()

for i in infos:
  city  = i.find("city").get_text()
  tmef  = i.find("tmef").get_text()
  wf = i.find("wf").get_text()
  tmn = i.find("tmn").get_text()
  tmx = i.find("tmx").get_text()
  cur.execute(insert_sql,(city,tmef,wf,tmn,tmx))

con.commit()  
con.close()