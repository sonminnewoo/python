# - 프록그램 설명 -
# 영화제목 / 평점 / 예매율 
# daum_movie 테이블 생성해서 추가 (스키마:pythondb)

# 웹페이지 크로링 라이브러리 불러오기 
import requests
from bs4 import BeautifulSoup

# import pymysql /> 밑에 추가 해둠 

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

# ▲ 위 처럼 접속할때 필요한 부분을 넣고 ,  con = pymysql.connect(host='127.0.0.1' , user='root', password='3123', 
                    #   db='pythondb' , charset='utf8') 부분에 필요한 부분을 넣어 버리면 된다


header =  {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://movie.daum.net/ranking/reservation' , headers=header)
soup = BeautifulSoup(req.content, 'html.parser')
txt = soup.select_one('#mainContent > div > div.box_ranking > ol')
# txt = soup.find('ol' , {'class' : 'list_movieranking'})
# print(txt)
lis = txt.select('li')


# MySQL 연결 라이브러리 불러오기
import pymysql

con = pymysql.connect(host='127.0.0.1' , user='root', password='3123', 
                      db='pythondb' , charset='utf8')
cur = con.cursor()

# 테이블 만들기 
# cur.execute("create table daum_movie(title char(200),lkie int,ticket int)")


# 데이터 넣는 방법(formet 이 스트링이라는것을 알려주는 것, 실행할때 (execute) )
insert_sql= "insert into daum_movie(title,lkie,ticket) values(%s, %s, %s)"

rows = []
for i in lis : 
    titles = i.find('a', class_='link_txt').get_text()
    lkies = i.find('span', class_='txt_grade').string
    tickets = i.find('span', {'class': 'txt_num'}).get_text()
    cur.execute(insert_sql,(titles,lkies,tickets))

# con.commit()
# # 단위 실행


# count 개수를 막대그래프로 표시

select_sql = "SELECT count,count(*) FROM COUNTTABLE group by count"
cur.execute(select_sql)
result = cur.fetchall()
x = []
y = []
for row in result:
    x.append(row[0])
    y.append(row[1])
con.close()

# 반환  
import matplotlib.pyplot as plt

# 한글 표시 안깨지게 하기 
import matplotlib as mpl
font_name = mpl.font_manager.FontProperties(fname = 'c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family = font_name)

# 막대그래프
plt.bar(x,y)
plt.title('음절 빈도 수 ')
plt.xlabel('음절')
plt.ylabel('개수')
plt.show()
# 파이 그래프
plt.pie(y, labels=x, autopct='%.1f%%')
plt.show()