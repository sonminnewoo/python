import sys, os, re, csv
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DAY2 import usecsv

# import usecsv

# apt_201910.csv 파일에서 3줄 출력
ap = usecsv.opencsv('apt_201910.csv')
apt = usecsv.switchcsv(ap)
print(apt[:3])
print(len(apt))

# 시군구 단지명 가격 ==> 6개 출력

# 지금 제일 처번째 줄에서 csv 를 읽어 온걸로 원하는 정보를 출력하는 내용을 출력하면 된다 
# ap = usecsv.opencsv('apt_201910.csv')

for i in apt[:6] : 
    print(i[0], i[4] , i[-4])

print('---------------------------------------')

# 강원도에 120 m2 이상 3억 이하 검색하기 시군구 단지명 가격 출력 

apt_list = [['시군구' ,'단지명', '가격']]
for i in apt :
    try:
        if i[5] >= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
        # 위에서match 말고 search 써도 된다 
            apt_list.append([i[0],i[5],i[-4]]) 
    except:
        pass

print(apt_list)
# 파일로 출력하기

with open('test012.csv','w',newline='') as f:
    # 파일 출력하는 방법 
    a = csv.writer(f, delimiter=',')
    # 저장하는 형식 과 저장하는 형식을 적어 준다 , 파일을 생성하는 줄
    a.writerows(apt_list)
    # 생성한 파일에 원하는 apt_list 의 값을 넣어준다

    # 여러 줄을 저장 하려고 하면은 writerows , 끝에 s 를 붙이고 
    # 한줄만 저장하려고 하면 writerow 을 쓴다 