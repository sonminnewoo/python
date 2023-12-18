import pandas as pd

#1. 나누고 
y1 = [100, 120, 150, 110]
y2 = [300, 120, 150, 110]
y3 = [600, 120, 150, 110]
y4 = [900, 120, 150, 110]
y5 = [1200, 120, 150, 110]
y6 = [1500, 120, 150, 110]

df = pd.DataFrame([y1,y2,y3,y4,y5,y6],
                 index = [2015,2016,2017,2018,2019,2020],
                 columns = ['1분기','2분기','3분기','4분기'])
#  데이터 프레임을 만들때 내부 데이터값을 지정해주고
# 인덱스와 , columns 항목을 만들어 준다 
df.to_csv('sales.csv', header=True)
#######그래프
import matplotlib.pyplot as plt
x = range(len(y1))
xLabel = ['final' , 'second', ' third', 'fourth']
plt.plot(x, y1, color='b')
plt.plot(x, y2, color='red')
plt.plot(x, y3, color='orange')
plt.plot(x, y4, color='green')
plt.plot(x, y5, color='brown')
plt.plot(x, y6, color='purple')
plt.xlabel('Quarters')
plt.ylabel('sales')
plt.title('2015~d2020 Quarters ')
plt.xticks(x,xLabel, fontsize=10)
plt.legend(['2015','2016','2017','2018','2019','2020'], loc='upper right')
plt.show()

########################
2. 
df2 = pd.DataFrame([[100, 120, 150, 110],[100, 120, 150, 110],[100, 120, 150, 110],
                   [100, 120, 150, 110],[100, 120, 150, 110],[100, 120, 150, 110]],
                   index = [2015,2016,2017,2018,2019,2020],
                columns = ['1a','2b','3c','4d'])
print(df2)

df2 = df2.transpose()
# 행과 열 을 바꿔주는 함수
x = range(len(df2[2015]))
plt.plot(x, df2[2015], color='b')
plt.legend()
plt.show()