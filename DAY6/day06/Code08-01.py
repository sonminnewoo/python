import pymysql

# naverdb 연결
con = pymysql.connect(host='127.0.0.1', user='root',     password='1234', db='naverdb', charset='utf8')
cur = con.cursor()

# 조회
while(True):
  data1 = input('사용자 ID ===>')
  if data1 =="":
    break
  data2 = input("사용자 이름 ==>")
  data3 = input("이메일 ==>")
  data4 = input ("출생년도 ===> ")

  # sql ="insert into userTable values('파이썬','파이썬이름','파이썬이메일',1999)" 
  sql ="insert into userTable values('"+data1 +"','"+data2+"','"+data3+"',"+data4+")" 
  cur.execute(sql)

con.commit()
con.close()  

