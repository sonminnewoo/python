# 파일 읽어와서 외국인 비율을 출력하고 싶음
# '구','한국인','외국인' , 외국인의 비율 출력 
# 구 는 이름 , 두번째 , 세번째 , 외국인
# 책에있는 파이썬에서 지원하는 파일 읽는 방식을 사용해도 되고 
# import csv 로 불러와도 된다 

import csv
import re
f = open('popSeoul.csv','r')
reader = csv.reader(f)
# 숫자 를 계산하려면 문자를 숫자로, 문자사이에 있는 ,도 제거 해야
# 한다
# 숫자에서 읽은 , 를 제거 해야 한다 
# 문자를 숫자(float)로 변환하기 

# 숫자에서 쉼표를 제거
output = [] 
for i in reader : 
    tmp = []
    for j in i :
        if re.search('\d',j) : #숫자라면 \d
            tmp.append(float(re.sub(',','',j))) # , j 에서 , 를 공백으로 바꾸고,float 형태로 담아라 
        else : # 
            tmp.append(j)
    # print(tmp) 이걸로 출력하면 실수로 출력까지는 된다
    output.append(tmp)
    # print(output[:6]) # 이걸로 출력하게되면 [[]] 의 형태로 출력하게 된다 
    # print(i[0], i[1], i[2])

# foreign2 = []
foreign2 = [] # 위 말고 이렇게 하면  
for i in output :

    foreign = 0 # 외국인 비율
    try: # 예외 처리
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        # print(foreign)
        if foreign > 5:
            foreign2.append([i[0],i[1],i[2],foreign])
        else :
            pass

    except : # 오류가 발생하면 처리할 것 ,
        pass

# '구','한국인','외국인' , 외국인의 비율 출력 5% 넘는거만 리스트에 담아 출력

print(foreign2)
########################################
test = [1,2,3,4,5]
print(test.index(5)) # 5의 위치값 
j = '1,468,246'
print(float(re.sub(',','',j)))
print(int(re.sub(',','',j)))