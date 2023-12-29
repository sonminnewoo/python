# 좋아요 수가 5만이하,  5만 이상 , 8만 이상, 10만 이상 ==> 파이 차트

import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt

# 제목 평점 예매율
dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser, passwd=dbPass,
                       db='pythondb', charset='utf8', use_unicode=True)
select_sql = "select likes from melon_se"

cur = conn.cursor()
cur.execute(select_sql)
likes = cur.fetchall()


# 평점이 9점이상, 8점이상, 6점이상, 6점미만 ==>pie

likesDic ={'10만이상':0, '8만이상':0, '5만이상':0, '5만이하':0}

for song in likes : 
    song = int(song[0])
    # print(movie)
    if song >= 100000 :
        likesDic['10만이상'] += 1
    elif song >=80000:  
        likesDic['8만이상'] += 1  
    elif song >=50000 :
        likesDic['5만이상'] += 1  
    else:
        likesDic['5만이하'] += 1  
print(likesDic)

#한글
font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure =  plt.figure()
axes = figure.add_subplot(111)
axes.pie(likesDic.values(), labels=likesDic.keys(), autopct='%.1f%%')
plt.show()