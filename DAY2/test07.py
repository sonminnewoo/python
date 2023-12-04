import csv
import re

def opencsv(filename):
    output = []
    f = open(filename,'r')
    reader = csv.reader(f)
    for i in reader:
        output.append(i)
    return output

total = opencsv('popSeoul2.csv')
for i in total[:5]:
    print(i)

for i in total[:5]:
    for j in i :
        try:
            i[i.index(j)] = float(re.sub(',','',j))
            # 순서대로 인덱스 값을 float 형태로 , 는 공백으로 반환한다
            # 하지만 숫자가 아니면 순자형으로 반환할수 없으니 
            # pass 하게 한다
        except:
            pass

print(total[:5])
