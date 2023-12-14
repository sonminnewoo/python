import pandas as pd

df = pd.read_csv('apt_201910.csv' , encoding='cp949',thousands=',')
print('################################')
print(len(df))
print(df.shape)
print(df.head(3))
print(df.tail())
#  면적만 출력
print(df['면적'])
print(df.면적)

# 면적이 130 보다 큰거 출력 
# print(df[df.면적>=130])
print(df[df.면적>200])
print('=-===================================')
# 단지명과 가격만 10개 출력
print(df.loc[:,['단지명','가격']])
print('=-===================================')
print(df.loc[:10,('단지명','가격')])

# 가격을 위에서 5개 출력
# print(df.loc[:,['가격']])
print(df.가격.head())
print(df['가격'].head())
# 면적이 130 넘는 아파트 가격만 
print(df.가격[df.면적>130].head(2))
# 면적이 130 넘고 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130)&(df.가격 < 20000)])
# thousands=',' 파일을 읽을때 , 를 없애준다
# 면적이 130 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130)|(df.가격 < 20000)])
# 가격 내림차순 으로 출력
df_desc = df.sort_values(by='가격',ascending=False)
print(df_desc.가격)
print(df.head(2))
# 9억원 을 초가하는 가격으로 거래하는 단지명(아파트),가격 출력
# df.loc[원하는 행의 조건, 원하는 열의조건]
print(df.loc[:,['단지명','가격']][df.가격>90000])
# 열(단가) 추가  가격 / 면적 
# 은 같지만 없는 칼럼을 생성할대는 반드시 df['단가'] aks rksmd 
# df.단가 는 읽을 때만 가능하고 , 새로 생성할대는 반드시 [] 안에 '단가'라고
# 해야 한다  아래 df.단가 = df.가격 / df.면적 할수 없다 
df['단가'] = df.가격 / df.면적
print(df['단가'])
print(df.loc[:10,('시군구','면적','단가')])
df1 = df.loc[:10,('시군구','면적','단가')]
df1.to_csv('apt_output.csv',index =False)
# 자동으로 단가 가 이런식의 지정만으로 추가 해준다 