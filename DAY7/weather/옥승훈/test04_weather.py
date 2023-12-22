# https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108
from bs4 import BeautifulSoup
import requests
import pymysql

con = pymysql.connect(host = '127.0.0.1', 
                      user = 'root', password = '3123', 
                      db = 'pythondb', charset = 'utf8')
cur = con.cursor()

req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108')
soup = BeautifulSoup(req.text, 'lxml')
wt = soup.find('location')
cname = soup.find_all('location')
row_in = wt.find_all('data')
insert_sql = "insert into forecast(city, tmef, wf, tmn, tmx) values(%s, %s, %s, %s, %s)"

wdata = []
for j in cname:
    city = j.find('city').get_text()
    for i in row_in:
        tmef = i.find('tmef').get_text()
        wf = i.find('wf').get_text()
        tmn = i.find('tmn').get_text()
        tmx = i.find('tmx').get_text()
        wdata.append([city, tmef, wf, tmn, tmx])
        cur.execute(insert_sql,(city, tmef, wf, tmn, tmx))
# print(wdata)

con.commit()
con.close()