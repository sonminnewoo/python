import pymysql

def insertData() :
    con , cur = None , None 
    data1, data2, data3 , data4 = "","" , "", "",
    sql=""
con = pymysql.connect(host='127.0.0.1', user='root', password='3123' , db='naverdb' , charset='utf8')
cur = con.cursor()

cur.execute("select * from userTable")
print('사용자ID 사용자 이름 사용자 이메일 사용자 번호')
print('---------------------------------------------')
while(True):
    row = cur.fetchone() # row 한개를 가져온다
    if row == None:
        break
    # 없으면 끝내는 구문 , 있으면 반복 , 
    data1 = row[0] # 사용자ID
    data2 = row[1] # 사용자 이름
    data3 = row[2] # 이메일
    data4 = row[3] # 출생연도
    # 매번 data1,2,3,4 값을 바뀔것 
    print("%5s %15s %15s %5d " % (data1, data2,data3,data4))
    # 그래도 바뀐 상태에서 바로 출력하니 상관 없이 잘출력 ㅗ딘다 
    # 문자열 5,15,15,숫자5 자리 의미를 하는것 

con.close()