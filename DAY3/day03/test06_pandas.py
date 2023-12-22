import pandas as pd
data = {
  'name' : ['aaa', 'bbb','ccc','ddd'],
  'age' : [33,44,55,66],
  'score' : [91.2, 88.7, 55.6, 77.2]
}
# dic  ==> DataFrame 으로
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.sum())
print(df['age'].mean())
print(df.age)
print(df['age'])