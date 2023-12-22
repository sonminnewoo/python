
# weather.csv 이나 weather_pandas.csv 를 읽어서 출력
# pandas 사용
import pandas as pd 
# df = pd.read_csv('weather_pandas.csv', encoding='utf-8-sig')
df = pd.read_csv('weather.csv', encoding='euc-kr')
print(df)
print(df.head())
print(df.columns.values)  # 헤더값 출력
print(df[' 기온'].mean())
# print(df.습도.mean())


