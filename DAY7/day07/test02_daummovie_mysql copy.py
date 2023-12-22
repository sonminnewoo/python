from bs4 import BeautifulSoup
import requests
import pymysql

# 제목 평점 예매율
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

con = pymysql.connect(host =dbURL , port = dbPort, user = dbUser, passwd = dbPass, db='pythondb', charset='utf8' )
req = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(req.content, 'html.parser')

ols = soup.find('ol', class_ = "list_movieranking")
movies = ols.find_all('div', class_ = "thumb_cont")

insert_sql="insert into daum_movie(title, grade, reserve) values(%s, %s, %s)"

# 1. insert
cur = con.cursor()

for i in movies:
  movietitle  = i.find("a", class_="link_txt").get_text()
  moviegrade  = i.find("span", class_="txt_grade").get_text()
  moviereserve = i.find("span", {'class' : 'txt_num'}).get_text()
  cur.execute(insert_sql,(movietitle,moviegrade,moviereserve))

con.commit()  
con.close()