import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

con = pymysql.connect(host =dbURL , port = dbPort, user = dbUser, passwd = dbPass, db='pythondb', charset='utf8' )  
cur = con.cursor()

# 한글
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font',family =font_name)


# 부산의 날짜별 최저기온 , 최고기온 plot 그래프
select_busan = "select * from forecast2 where city='부산'"
cur.execute(select_busan)
result_plot = cur.fetchall() 
low = [] # 최저기온
high = [] # 최고기온
xdata = [] # 날짜
for r in result_plot:
  low.append(r[4])
  high.append(r[5])
  xdata.append(r[2])

plt.figure(figsize=(8,6))
plt.plot(xdata,low,label = '최저기온')
plt.plot(xdata,high,label = '최고기온')
plt.xticks(rotation=25)
plt.title("중기 부산 기온 예보")  
plt.legend()
plt.show() 

# 부산 wf 상태를 막대(bar), 파이(pie) 차트로 출력
select_busan1 = "select wf,count(*) from forecast2 where city='부산' group by wf"
cur.execute(select_busan1)
result_busan = cur.fetchall()
print(result_busan)
x = []
y = []
for r in result_busan:
  x.append(r[0])
  y.append(r[1])

plt.bar(x, y)  
plt.show()
####
plt.pie(y, labels=x, autopct='%.1f%%')
plt.show()



