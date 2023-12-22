import pymysql

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"

con = pymysql.connect(host =dbURL , port = dbPort, user = dbUser, passwd = dbPass, db='pythondb', charset='utf8' )  
cur = con.cursor()

# 부산의 정보 추출
select_busan= "select * from forecast2 where city = '부산' order by tmef desc"
cur.execute(select_busan)
result_busan = cur.fetchall()
print(result_busan)

# 부산의 날짜 최저기온 , 최고기온
select_busan1 = "select min(tmn), max(tmx) from forecast2 where city = '부산'"
cur.execute(select_busan1)
result_busan1 = cur.fetchone()
print(result_busan1)
print('최저기온 : ',result_busan1[0])
print('최고기온 : ',result_busan1[1])

# 날짜별 최고기온,최저기온 출력
datas = []
for row  in result_busan:
  datas.append([row[2], row[4],row[5]])
print(datas)  

