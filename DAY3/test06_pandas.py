import pandas as pd

data = {
    'name' : ['aaa','bbb','ccc','ddd'],
    'age' : [33,44,55,66],
    'score' : [91.2 , 88.7 , 55.6 ,77.2]
}

# dic ==> DataFrame 으로 
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum())
print(df['age'].mean())
# 평균을 구하는 펑션에서 문자를 넣어 오류 발생 
# df.mean() 으로 하면 에러 발생 하기 때문에 print(df['age'].mean()) 이런 
# 형식 으로 해주면 출력된다 
print(df.age)
print(df['age'])