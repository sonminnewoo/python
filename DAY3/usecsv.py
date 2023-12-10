# csv 사용 // 미사용한건 Code06-1,3,5 라는 파일
import csv
import re

# 함수 선언할때 파일네임 받는 거를 지정하지 않음 
def opencsv(filename):
    output = []
    f = open(filename,'r')
    reader = csv.reader(f)
    for i in reader:
        output.append(i)
    return output

def switchcsv(listName):
    for i in listName:
        for j in i:
            # 위에 i 에 listName 로 지정하면 값이 변경되지 않는다 
            try:
                i[i.index(j)] = float(re.sub(',','',j))
            except:
                pass
      
    return listName