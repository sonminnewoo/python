import pymysql

# naverdb 연결
con = pymysql.connect(host='127.0.0.1', user='root',     password='1234', db='naverdb', charset='utf8')
cur = con.cursor()

cur.execute("select * from userTable")
print("사용자ID    사용자이름    이메일            출생연도")
print('------------------------------')
while(True):
  row = cur.fetchone()
  if row == None:
    break
  data1 = row[0]  # 사용자ID
  data2 = row[1]  # 사용자이름
  data3 = row[2]  # 이메일
  data4 = row[3]  # 출생연도
  print("%5s %15s  %15s %5d " % (data1, data2, data3, data4))

con.close()  
