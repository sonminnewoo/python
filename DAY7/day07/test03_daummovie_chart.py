import pymysql
import matplotlib.pyplot as plt 


# 제목 평점 예매율
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

con = pymysql.connect(host =dbURL , port = dbPort, user = dbUser, passwd = dbPass, db='pythondb', charset='utf8' )

select_sql="select grade from daum_movie"
cur = con.cursor()
cur.execute(select_sql)
movies = cur.fetchall()
# 평점이 9점이상, 8점이상, 6점이상, 6점미만 ==>pie
movieDic = {'9점이상' : 0 , '8점이상': 0 , '6점이상' : 0, '6점미만' : 0}
for movie in movies:
  movie =float(movie[0]) 
  if movie >= 9:
    movieDic['9점이상'] += 1
  elif movie >= 8:
    movieDic['8점이상'] += 1  
  elif movie >= 6:
    movieDic['6점이상'] += 1
  else:
    movieDic['6점미만'] += 1
print(movieDic)    
con.commit()  
con.close()

# 그래프
# 한글 
import matplotlib as mpl 

font_name = mpl.font_manager.FontProperties(fname ='c:/Windows/fonts/malgun.ttf').  get_name()
mpl.rc('font', family =font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(movieDic.values(), labels=movieDic.keys(), autopct='%.1f%%')
plt.show()