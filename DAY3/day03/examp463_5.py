# 이름 나이 생일 
# 하나 유정 30   1991.5.2 
# 둘   유나 28   1993.4.6 
# 셋   민영 31   1990.9.12 
# 넷   은지 29   1992.7.19

## 5번
import pandas as pd 
data = { '이름' : ['유정', '유나', '민영', '은지'], 
          '나이' : [30, 28, 31, 29], 
          '생일' : ['1991.5.2', '1993.4.6', '1990.9.12', '1992.7.19'] } 
index_data = ['하나', '둘', '셋', '넷'] 
# dic ==> DataFrame
df =pd.DataFrame(data, index_data)  # df =pd.DataFrame(data, index = index_data) 
print(df)

# 6번 
import matplotlib.pyplot as plt 
x_data =[10,20,30,40,50]
y_data =[1000,1500,3000,3000,6000]
plt.plot(x_data, y_data, color='green', linestyle=":", marker='o')
plt.show()

# 7번  민영 출력
print(df.loc['셋','이름'])
# print(df.iloc['셋','이름'])  ==> 오류발생 iloc  위치값으로 
print(df.loc['셋'],['이름'])
print(df.iloc[2,0])



