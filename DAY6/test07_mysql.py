# mySQL 을 연결해주는 그무언가 가 필요하다 
# 이것을 연결해주는 패

import pymysql


# MySQL 에 원하는 유저 ,에 연결한다 
# 가장 먼저 root 에 연결한다 
con = pymysql.connect(host='127.0.0.1', user='root',
                       password='3123' , db='naverdb' , charset='utf8')
#  connect 라고 정확히 표기 해줘야 한다 , charset='utf8' 으로 한다 
# 위가 실행되면 연결이된것이다 />> 이때 con 은 연결된 객체 이다
cur = con.cursor()
#  그 객체를 지정해서 ,cursor() 을 얻는다
cur.execute("create table userTable(id char(4),userName char(15), email char(20), birthYear int)")
# 위에 새로 테이블을 만드는 내용이다 

cur.execute("insert into userTable values('john' , 'john Bann' , 'john@naver.com',1990)")
# userTable 위에서 만들 테이블에 값을 넣는것이다 

con.commit()
# 단위 실행
con.close()
# 반환  
