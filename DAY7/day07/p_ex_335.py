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
con = pymysql.connect(host='127.0.0.1', user='root', password='1234', database='pythondb', charset='utf8') 
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS countTable")
cur.execute("CREATE  TABLE  countTable(onechar  varchar(10) , count INT)") # 문자, 개수

for ch in inStr :
    if  'ㄱ' <= ch <= '힣' :
        cur.execute("SELECT * FROM countTable WHERE onechar = '" + ch + "'")
        row = cur.fetchone()
        if row == None :
            cur.execute("INSERT INTO countTable VALUES('" + ch + "'," + str(1) + ")")
        else :
            cnt = row[1]
            cur.execute("UPDATE countTable SET count =" + str(cnt+1) + " WHERE onechar = '" + ch + "'")

con.commit()
    
cur.execute("SELECT * FROM countTable order by count DESC")
print('원문\n', inStr)
print('-------------------------')
print('문자\t빈도수')
print('-------------------------')

while (True) :
    row = cur.fetchone()
    if row== None :
        break;
    ch = row[0]
    cnt = row[1]
    print("%4s   %5d" % (ch, cnt))

# count 개수를 막대그래프로 표시    
select_sql ="SELECT  count, count(*) from counttable group by count"
cur.execute(select_sql)
result = cur.fetchall()


x = []
y = []
for row in result:
    x.append(row[0])
    y.append(row[1])
    
con.close()

import matplotlib.pyplot as plt 
import matplotlib as mpl 
# 한글 
font_name = mpl.font_manager.FontProperties(fname ='c:/Windows/fonts/malgun.ttf').  get_name()
mpl.rc('font', family =font_name)
# 막대그래프
plt.bar(x, y)
plt.title('음절 빈도 수')
plt.xlabel('음절')
plt.ylabel('개수')
plt.show()

#파이 그래프
plt.pie(y, labels=x, autopct='%.1f%%')
plt.show()
