# 평점이 9점 이상, 8점 이상 , 6점 이상 ,6점미만 ==> pie
import pymysql
# mysql 연결하기 위해 라이브러리 읽어 오기
import matplotlib.pyplot as plt
# 파이 차트 만들기 위해 라이브러리 불러오기

import matplotlib.font_manager as fm
import matplotlib as mpl
# 한글 폰트가 깨지는 경우 폰트 라이브러리를 불러온다 

font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
fontprop = fm.FontProperties(fname=font_path, size=12)
# 불러온 라이브러리를 원하는 형식으로 지정해준다
# 자세히 보면 font_manager 라는게 matplotlib 의 하위로 되어있기 때문에 제대로
# 인식이 되게 될것이다 

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "3123"

# ▲ 위 처럼 접속할때 필요한 부분을 넣고 ,  con = pymysql.connect(host='127.0.0.1' , user='root', password='3123', 
                    #   db='pythondb' , charset='utf8') 부분에 필요한 부분을 넣어 버리면 된다 ▼
con = pymysql.connect(host=dbURL , port= dbPort ,user=dbUser, password=dbPass, 
                      db='pythondb' , charset='utf8')
# select_sql = "select * from daum_movie"
select_sql = "select lkie from daum_movie"
cur = con.cursor()

cur.execute(select_sql)
result = cur.fetchall()
# 모든 행을 읽을때는 fetchall()
# 한줄만 읽을 때는 fetchone()   
label = ['9점이상','8점이상','6점이상','6점미만']
columcount = [0,0,0,0]

for row in result :
    movie = float(row[0])
#   위를 안해주면 비교 하는 if 비교구문이 제대로 동장하지 않기 때문 바꿔준다
    if movie >= 9:
        columcount[0] += 1
    elif movie >= 8:
        columcount[1] += 1
    elif movie >= 6:
        columcount[2] += 1
    else:
        columcount[3] += 1

font_name = mpl.font_manager.FontProperties(fname = 'c:/Windows/fonts/malgun/ttf').get_name()
mpl.rc('font', family = font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
axes.title('영화 평점 분포')
axes.show()

# plt.pie(columcount, labels=label, autopct='%1.1f%%', startangle=90)
# plt.title('영화 평점 분포', fontproperties=fontprop)
# plt.show()
    

con.commit()
con.close()