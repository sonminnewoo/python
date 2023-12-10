import re 
import csv

#  apt_201910.csv 파일에서 3줄 출력

def opencsv(filename):  # filename  = apt_201910.csv
  output = []
  f =  open(filename, 'r')
  reader = csv.reader(f)
  for i in reader:
       output.append(i)
  return output


def switchcsv(listName):
  for i in listName:
     for j in i:
        try:
           i[i.index(j)] = float(re.sub(',','',j))
           
        except:
           pass
    
  return listName

ap = opencsv('apt_201910.csv')  # apt_201910.csv 을 읽어서 리스트에 담기
apt = switchcsv(ap)  # 리스트에 있는 ,  제거하고 float 형태로 변환
print(apt[:3])
print(len(apt))

#시군구 단지명 가격 =>6개 출력
for i in apt[:6]:
    print(i[0], i[4], i[-4])
print('-----------')
# 강원도에 120m2 이상 3억 이하 검색하기 시군구 단지명 가격 출력
apt_list = []

print(apt_list)
for i in apt:
    try:
        if i[5]>= 120 and i[-4] <= 30000 and re.match('강원', i[0]):
            apt_list.append([i[0], i[5], i[-4]])
    except:
       pass  

print(apt_list)
#파일로 출력 apt_out.csv
import csv
with open('apt_out.csv','w',newline='')as f:
   a = csv.writer(f, delimiter=',')
   a.writerows(apt_list)
