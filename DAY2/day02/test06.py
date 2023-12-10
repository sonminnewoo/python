
import csv
import re

f = open('popSeoul.csv','r')
reader = csv.reader(f)
# 숫자,(천단위) 를 제거하기
# 문자를 숫자(float)로 변환하기
output=[]
for i in reader:
  tmp = []
  for j in i:
    if re.search('\d', j) : # 숫자라면
      tmp.append(float(re.sub(',','',j)))
    else : 
      tmp.append(j)
  # print(tmp)
  output.append(tmp)   
  # print(output)

# '구', '한국인', '외국인', '외국인 비율(%)'    
#  '외국인 비율(%) 이 5%로 넘는것만 리스트에 담아 출력
result = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in output:
  foreign = 0
  try:
    foreign = round(i[2]/(i[1]+i[2])*100,1)
    print(foreign)
    if foreign > 5:
      result.append([i[0], i[1], i[2],foreign] )
  except:
    pass

print(result)
############# 
test = [1, 2, 3, 4, 5]
print(test.index(5))
j = '1,468,246'
print(float(re.sub(',','',j)))
print(int(re.sub(',','',j)))  