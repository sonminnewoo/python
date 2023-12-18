import pymysql

# naverdb 에 연결
con = pymysql.connect(host='127.0.0.1', user='root',
                       password='3123' , db='naverdb' , charset='utf8')
cur = con.cursor()

# 조회
while(True) : 
    data1 = input('사용자 ID ===>') 
    if data1 =="":
        break
    data2 = input('사용자 이름==>')
    data3 = input('이메일==>')
    data4 = input('출생년도==>')
    # sql ="INSERT INTO userTable (아이디, 이름,이메일,출생년도) VALUES (%s, %s %s ,%s)"
    # sql ="INSERT INTO userTable values('파이썬','파이썬이름','이메일','1999)" 를 표현하는것 아래를 표현한것이다 
    # sql ="INSERT INTO userTable values('",파이썬,"','",파이썬이름,"','",이메일,"',1999)"

    # sql ="INSERT INTO userTable values('",data1,"','",data2,"','",data3,"'",data4,")"
    sql ="INSERT INTO userTable values('"+data1+"','"+data2+"','"+data3+"',"+data4+")"
    cur.execute(sql)
    # values = (data1,data2,data3,data4)
    # cur.execute(sql,values)

con.commit()
con.close()