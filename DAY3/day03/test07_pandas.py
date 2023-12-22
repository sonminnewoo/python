# year   sales
# 2018 350
# 2019 400
# 2020 1050
# 2021 2000
# 2022 1000
# 2023 2500
import pandas as pd 
data_dic = {
  'year' : [2018, 2019, 2020, 2021, 2022, 2023 ],
  'sales' : [350, 400, 1050, 2000, 1000,2500]
}
print(data_dic)
# dic ==> DataFrame 형으로
df = pd.DataFrame(data_dic) 
print(df)

df2 = pd.DataFrame([[89.2, 92.5, 90.8],[92.8, 89.9, 95.2]],
                   index=['중간고사', '기말고사'],
                   columns=['1반', '2반', '3반'])
print(df2)

df3 =pd.DataFrame([[20201101,'Kim',100,90],
                   [20201102,'Park',85,70],
                   [20201102,'Hong',66,44],
                   [20201102,'Lee',55,72]],
                  columns=['학번', '이름', '중간고사', '기말고사'])
print(df3)
print('중간고사 합계  : ',df3.중간고사.sum())
print('기말고사 합계  : ', df3.기말고사.sum())
# 컬럼에 총점 추가
df3['총점'] = df3.중간고사 + df3.기말고사
print(df3)
print('시험평균 : ' , df3.총점.mean())

df4 =pd.DataFrame([[20201101,'Kim',100,90],
                   [20201102,'Park',85,70],
                   [20201102,'Hong',66,44],
                   [20201102,'Lee',55,72]])
print(df4)
df4.columns = ['학번', '이름', '중간고사', '기말고사']
print(df4)
print(df4.tail(2))
# df3을 pandas03.csv 파일로 내보내기
df3.to_csv('pandas07.csv', index=False)

# pandas03.csv 읽어와서  출력 print 하기
df7 =pd.read_csv('pandas07.csv', encoding='utf-8')
print(df7)