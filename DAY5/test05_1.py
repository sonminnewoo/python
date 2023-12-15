import bs4
import pandas as pd

# 여러가지 이상한 읽는 방식이 있지만 ▼ 아래 방식을 이용하면 가장 편하다
csv_read1 = pd.read_csv('weather.csv', encoding='utf-8-sig')
# pandas 를 쓰면 그냥 알아서 통째로 읽어온다 
print(csv_read1)
print(csv_read1.head())
print(csv_read1['기온'].mean())
# 평균을 내는 방법 1
print(csv_read1.습도.mean())
# 평균을 내는 방법 2

# weather.csv

# 기존의 방식으로 읽는것 
# header = inFp.readline() # inFp 파일을 한줄 읽고
# header = header.strip() # 읽은걸 공백제거하고
# header_list = header.split(',') # 헤더 지정하고 split 문자열을 끊어서 header_list 에 넣고 

# with open('weather.csv','w', newline='', encoding='utf-8') as file:
#     file.write('지역,기온,습도\n')
#     for item in datas :
#         row = ','.join(item)
#         file.write(row+'\n')


# # weather_pandas.csv
# import pandas as pd
# df_weather = pd.DataFrame(datas,columns = ('지역','기온','습도'))
# df_weather.to_csv('weather_pandas.csv', encoding='utf=-8-sig',index=False)