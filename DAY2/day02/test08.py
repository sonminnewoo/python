import usecsv

total  =usecsv.opencsv('popSeoul.csv')
nlist = usecsv.switchcsv(total)
print(nlist[:5])

result = [['구', '한국인', '외국인', '외국인비율(%)']]
for i in nlist:
  foreign = 0
  try:
    foreign = round(i[2]/(i[1]+i[2])*100,1)
    if foreign > 7 :
      result.append([i[0], i[1], i[2], foreign])
  except:
    pass
print(result)  

# result 리스트를 문자열로 변환
row_str = ','.join(map(str, result))
# result 를 파일(foreign.csv)로 내보내기
with open('foreign.csv', 'w') as outFp:
  outFp.write(row_str+'\n')

import csv
with open('foreign11.csv', 'w', newline='') as f:
  a = csv.writer(f)
  a.writerows(result)


