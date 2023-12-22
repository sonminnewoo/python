import pandas as pd 

df = pd.read_csv('apt_201910.csv',encoding='cp949',thousands=',')
print(len(df))
print(df.shape)
print(df.head())
print(df.tail())
print('------------')
# 면적만 출력
print(df['면적'])
print(df.면적)
# 면적이 200보다 큰 거 출력
print(df[df.면적>200])
print('------------')
# 단지명, 가격만 출력
print(df.loc[:, ['단지명', '가격']])
# 단지명, 가격만 10개 출력
print(df.loc[:10, ['단지명', '가격']])
print(df.loc[:10, ('단지명', '가격')])

# 가격을 위에서 5개 출력
print(df['가격'].head())
print(df.가격.head())
# 면적이 130 넘는 아파트의 가격만 출력
print(df.가격[df.면적>130])
# 면적이 130 넘는 아파트의 가격만 위에서 5개 출력
print(df.가격[df.면적>130].head())
# 면적이 130 넘고 가격이 2억 미만인 아파트의 가격 출력
# 가격에 , 있어 문자열로 인식 ==> 오류발생
print(df.가격[(df.면적>130) & (df.가격 < 20000)])

# 면적이 130 넘거나 가격이 2억 미만인 아파트의 가격 출력
print(df.가격[(df.면적>130) | (df.가격 < 20000)])
# 가격 내림차순으로 출력
df_desc = df.sort_values(by='가격', ascending=False)
print(df_desc.가격)
print(df.head())
# 9억원을 초과하는 가격으로 거래된 단지명(아파트), 가격 출력
# df.loc[원하는 행의 조건, 원하는 열의조건]
print(df.loc[:,['단지명', '가격']][df.가격 > 90000])
# 열(단가) 추가    가격 / 면적
#  df.단가 df['단가]은 같지만 없는 컬럼을 생성할때는 반드시 df['단가']만 가능
# df.단가 = df.가격 /  df.면적  ==> 없는 컬럼이므로 안됨
df['단가'] = df.가격 /  df.면적
print(df['단가'])
print(df.loc[:10 , ('시군구', '면적', '단가')])
df1 = df.loc[:10 , ('시군구', '면적', '단가')]
df1.to_csv('apt_output.csv', index =False)