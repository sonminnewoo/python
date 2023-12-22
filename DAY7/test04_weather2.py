from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
# # https://www.weather.go.kr/w/weather/forecast/mid-term.do

soup = BeautifulSoup(req.text, 'lxml')

# SQL 관련
import pymysql
con = pymysql.connect(host='127.0.0.1' , user='root', password='3123', 
                      db='pythondb' , charset='utf8')
cur = con.cursor()
# MySQL 에 테이블 추가 ▼
# cur.execute("CREATE TABLE forecast2(city VARCHAR(500), tmef VARCHAR(500), wf VARCHAR(500),tmn VARCHAR(500),tmx VARCHAR(500))")

insert_sql = "INSERT INTO forecast2(city, tmef, wf, tmn, tmx) value(%s, %s, %s, %s, %s)"

for i in soup.find_all('location'):
    city = i.find('city').text
    for j in i.find_all('data') : 
        tmef = j.find('tmef').text
        wf = j.find('wf').text
        tmn = j.find('tmn').text
        tmx = j.find('tmx').text
        cur.execute(insert_sql, (city,tmef,wf,tmn,tmx))

# 항목 별로 자료 를 추가한다, 이때 열 은 city 기준 이다
# 파이썬 계시판 만드는 거 할줄 알아야한다

con.commit()
con.close()