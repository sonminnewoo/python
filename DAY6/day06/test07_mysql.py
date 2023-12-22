import pymysql

con = pymysql.connect(host='127.0.0.1', user='root',                         password='1234', db='naverdb', charset='utf8')

cur = con.cursor()
cur.execute("create table userTable(id char(4), userName char(15), email char(20), birthYear int )")

cur.execute("insert into userTable values('john', 'John Bann','john@naver.com', 1990)")

con.commit()
con.close()