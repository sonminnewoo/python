import csv
#첫번재 행에 ['컴퓨터', '노트북', '태블릿']
#두번째 행에 [100, 80,60]
#리스트 형태로 표현
test_list[['컴퓨터', '노트북', '태블릿'],[100, 80,60]]
print(test_list)
#csv를 이용해 파일(test.csv)로 출력

with open('test.csv', 'w', newline='') as f :
    a= csv.writer(f, delimiter=',')
    a.writerows(test_list)