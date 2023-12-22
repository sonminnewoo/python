import pymysql

## 전역 변수 선언 부분 ##
inStr = '''죽는 날까지 하늘을 우러러 한 점 부끄럼이 없기를,
잎새에 이는 바람에도 나는 괴로워했다.
별을 노래하는 마음으로 모든 죽어가는 것을 사랑해야지.
그리고 나한테 주어진 길을 걸어가야겠다.
오늘 밤에도 별이 바람에 스치운다. '''
con, cur = None, None
onechar, count = "", 0
## 메인 코드 부분 ##
con = pymysql.connect(host='127.0.0.1', user='root', password='3123', database='pythondb', charset='utf8') 
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS countTable")
cur.execute("CREATE  TABLE  countTable(onechar  varchar(10) , count INT)") # 문자, 개수

for ch in inStr :
    if  'ㄱ' <= ch <= '힣' :
        # 한글일때 
        cur.execute("SELECT * FROM countTable WHERE onechar = '" + ch + "'")
        # 읽고
        row = cur.fetchone()
        # 행에 새로운 해을 넣고 
        if row == None :
            # 거기에 값이 없으면 
            cur.execute("INSERT INTO countTable VALUES('" + ch + "'," + str(1) + ")")
            # 값에 1 넣고 
        else :
            # 값이 있으면
            cnt = row[1]
            # cnt 는 행의 값 열 을 선택
            cur.execute("UPDATE countTable SET count =" + str(cnt+1) + " WHERE onechar = '" + ch + "'")
            # 읽은 수만은 글중 WHERE onechar = '" + ch + "'" 에서 만 ! 1개 이중복없는(SET) 으로 기존 값에 +1 해서 

con.commit()
    
cur.execute("SELECT * FROM countTable order by count DESC")
# count 를 기준으로 정렬 해준다
print('원문\n', inStr)
print('-------------------------')
print('문자\t빈도수')
print('-------------------------')

while (True) :
    row = cur.fetchone()
    # cur 에서 한행을 읽어서 row 에 넣고 
    # row 에 값이 없으면 
    if row== None :
        break;
    # 위는 없을때 까지 계속 읽는것

    ch = row[0]
    cnt = row[1]
    # 값 부분에 원하는 값을 업데이트 해준다 
    print("%4s   %5d" % (ch, cnt))

# count 개수를 막대그래프로 표시    
 
# GRUOPBY 같은걸로 묶어 준다

