import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from day02 import usecsv
import re

# apt_201910.csv 파일에서 3줄 출력
ap = usecsv.opencsv('apt_201910.csv')
apt = usecsv.switchcsv(ap)
print(apt[:3])
print(len(apt))

# 시군구 단지명  가격 ==> 6개 출력
for i in apt[:6]:
  print(i[0], i[4],i[-4])
print('-----')
# 강원도에 120 m2 이상 3억 이하 검색하기 시군구 단지명  가격 출력
apt_list = [['시군구', '단지명', '가격']]  # 시군구, 단지명, 가격 
for i in apt:
  try:
    if i[5] >=120 and i[-4] <= 30000 and re.match('강원', i[0]):
      apt_list.append([i[0], i[5], i[-4]])
  except:
    pass

print(apt_list)
# 파일로 출력 apt_out.csv
import csv
with open('apt_out.csv', 'w', newline='') as f:
  a = csv.writer(f, delimiter=',')
  a.writerows(apt_list)

