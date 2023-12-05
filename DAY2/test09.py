import csv
# 첫번째 행에 컴퓨터 ,노트북 ,태블릿
# 두번째 행에 100,80 , 60
# 리스트 형태로 표현 


test_list = [['컴퓨터','노트북','태블릿'], [100,80 , 60]]
print(test_list)

# 위 를 csv 로 출력

# row_str = ','.join(map(str,test_list))
with open('test09.csv','w',newline='') as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(test_list)