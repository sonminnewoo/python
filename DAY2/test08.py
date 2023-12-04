import usecsv

total = usecsv.opencsv('popSeoul.csv') # 함수 opencsv 을 이용해서 읽을 파일 지정
# 그걸 total에 넣고 
# total 은 nlist 에 switchcsv 함수로 입력 해준다 
nlist = usecsv.switchcsv(total)
print(nlist[:4])
# 위는 얼마나 nlist 에서 읽어올지 를 지정해주는 것 

result = [['구','한국인','외국인','외국인비율(%)']]
for i in nlist:
    foreign = 0
    try :
        foreign = round(i[2]/(i[1]+i[2])*100,1)
        if foreign>7:
            result.append(i[0],i[1],i[2],foreign)
    except:
        pass

print(result)

# result 리스트를 문자열로 변환 
row_str = ','.join(map(str,result))

# result 를 파일 (foreign.csv) 로 내보내기 
# Code06 형태로 작성
with open('foreign.csv' , 'w') as outFp:
    outFp.write(row_str+'\n')

import csv
with open('foreign11.csv' , 'w') as f:
    a = csv.writer(f)
    a.writerow(result)