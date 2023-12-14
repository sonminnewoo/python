# 이름 나이 생일
# 하나 유정 30 1991.5.2
# 둘 유나 28 1993.4.6
import pandas as pd

data = {
    '이름' : ['유정','유나','민영','은지'],
    '나이' : [30,28,31,29],
    '생일' : ['1991.5.2','1993.4.6','1991.5.2','1993.4.6']
}
index_data = ['하나','둘','셋','넷']

# dic ==> DataFrame
df = pd.DataFrame(data, index=index_data)
print(df)

#6번
import matplotlib.pyplot as plt

x_data = [10,20,30,40,50]
y_data = [1000,1500,3000,3000,6000]

plt.plot(x_data , y_data , color='green' , linestyle=":",marker='o')
plt.show()

# 7번 민영 출력
print(df.loc['셋','이름'])
#print(df.iloc['셋','이름'])   ==> 오류 발생 
print(df.loc['셋'],['이름'])
print(df.iloc[2,0])
# 인덱스의 위치 값을 지정 한다 0 부터 시작할대 3번째 위치 의 민영을
# 출력해준다 . 행과 열을 지정하는 방식으로 