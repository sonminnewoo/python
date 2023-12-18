import pandas as pd

df = pd.read_csv('weather.csv' , encoding='utf-8-sig' , index_col='지역')
 # 기준을 지역 중심으로 하겠다는 지정
print(df)
# 서울,인천, 대구, 광주 , 부신
# print(df.loc[['서울', '부산']])
# print(df.loc[['서울', '인천','대전', '대구','광주', '부산']])
city_df = df.loc[['서울', '인천','대전', '대구','광주', '부산']]

#그래프 
import matplotlib.pyplot as plt
# 한글을 사용하기 위해서는 아래처럼 그자체를 불러와서 사용 해줘야 한다  
import matplotlib as mpl

# 한글 처리 먼저
font_name = mpl.font_manager.FontProperties(fname ='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family = font_name)
ax = city_df.plot(kind='bar' , title='날씨' , figsize=(9,6),fontsize=12 , legend=True)
# 범롈를 지정해주면 내용에 대한 간략한 설명을 해준다 
ax.set_xlabel('도시')
ax.set_ylabel(['기온','습도'])
plt.show()

####################### 막대 그래프
figure = plt.figure()
axes = figure.add_subplot(111)
xdate = ['서울', '인천','대전', '대구','광주', '부산']
axes.bar(xdate,city_df['기온'],label= '기온')
# 하나의 그래프에 대한 내용 : 기온
axes.bar(xdate,city_df['습도'],label= '습도')
# 하나의 그래프에 대한 내용 : 습도
plt.legend(['습도','기온'])
# 두개를 한개로 표현하는 형식
plt.show()

####################### 꺽은선 그래프
figure = plt.figure()
axes = figure.add_subplot(111)
xdate = ['서울', '인천','대전', '대구','광주', '부산']
axes.plot(xdate,city_df['기온'],label= '기온')
axes.plot(xdate,city_df['습도'],label= '습도')
plt.legend(['습도','기온'])
plt.show()

# 꺽은선 그래프
