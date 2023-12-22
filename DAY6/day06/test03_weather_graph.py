import pandas as pd 

df = pd.read_csv('weather18.csv', encoding='utf-8-sig', index_col='지역')
print(df)
# 서울, 인천, 대전, 대구, 광주, 부산
# print(df.loc[['서울','부산']])
# print(df.loc[['서울','인천','대전','대구','광주','부산']])
city_df = df.loc[['서울','인천','대전','대구','광주','부산']]

# 그래프
import matplotlib.pyplot as plt
import matplotlib as mpl 

# 한글
font_name = mpl.font_manager.FontProperties(fname ='c:/Windows/fonts/malgun.ttf').  get_name()
mpl.rc('font', family =font_name)
mpl.rcParams['axes.unicode_minus'] = False 

ax = city_df.plot(kind='bar',title='날씨', figsize=(9,6),fontsize=12, legend=True)
ax.set_xlabel('도시')
ax.set_ylabel(['기온', '습도'])
plt.show()

########## 막대그래프
figure = plt.figure()
axes = figure.add_subplot(111)
xdata = ['서울','인천','대전','대구','광주','부산']
axes.bar(xdata,city_df['기온'])
axes.bar(xdata,city_df['습도'])
plt.legend(['습도','기온'])
plt.show()
########
figure = plt.figure()
axes = figure.add_subplot(111)
xdata = ['서울','인천','대전','대구','광주','부산']
axes.plot(xdata,city_df['기온'], label = '기온')
axes.plot(xdata,city_df['습도'], label = '습도')
plt.legend()
plt.show()

