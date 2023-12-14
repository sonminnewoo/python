# year sales
#2018 350
#2019 400
#2020 1050
#2021 2000
#2022 1000
#2023 2500
import pandas as pd

data_dic = { 
    # 키 값
    'year' : ['2018','2019','2020','2021','2022','2023'],
    # 벨류 값
    'sales' : [350,400,1050,2000,1000,2500]
}

print(data_dic)

# dic ==> dataFrame 형식으로

df = pd.DataFrame(data_dic)
print(df)

df2 = pd.DataFrame([[89.2, 92.5, 90.8],[89.2, 92.5, 90.8]],
                    index=['중간고사','기말고사'],
                    columns=['1반','2번','3반'])
print(df2)

df3 = pd.DataFrame([[20201101, 'kim',100,90],
                    [20201101, 'kim',100,90],
                    [20201101, 'kim',100,90],
                    [20201101, 'kim',100,90]],
                    columns=['학번','이름','중간고사','기말고사'])
print(df3)
print('중간고사 합계 : ', df3.중간고사.sum())
print('기말고사 합계 : ', df3.기말고사.sum())
# 컬럼에 '총점' 추가 
df3['총점'] = df3.중간고사 + df3.기말고사
print(df3)
print('시험평균 : ', df3.총점.mean())

df4 = pd.DataFrame([[20201101, 'kim',100,90],
                    [20201101, 'kim',100,90],
                    [20201101, 'kim',100,90],
                    [20201101, 'kim',100,90]])

print(df4)
df4.columns = ['학번','이름','중간고사','기말고사']
print(df4)

#df3 을 pandas03.csv 파일로 내보내기
df3.to_csv('pandas07.csv' , index=False)
# index 앞에 인덱스 부분을 표시 하고 싶지 않으면 index=False 로 출력해준다 

#pandas03.csv 읽어와서 출력 print 하기
df7 = pd.read_csv('pandas07.csv')
print(df7)