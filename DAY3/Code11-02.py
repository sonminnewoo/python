import numpy as np
import matplotlib.pyplot as plt
# matplotlib 막대 그래프를 만들어주는 라이브 러리 
# 실제 실행하면 그래프 를 표시 해준다 

x_data = ['1sh','2sh','3sh','4sh','5sh']
x_value = np.array([1,2,3,4,5])
y1_data = np.array([90,28,75,58,78])
y2_data = np.array([80,80,50,40,90])
y3_data = np.array([40,50,90,90,60])

plt.bar(x_value, y1_data, color = 'red' , width=0.1 , label='Dahyon')
plt.bar(x_value+0.2, y2_data, color = 'green', width=0.1,label='Jungyon')
# x_value 에 +0.2 를 하면 옆으로 이동한다 , width=0.1 넓이를 부여해준다 
plt.bar(x_value+0.4, y3_data, color = 'blue', width=0.1,label='MoMo')
plt.xticks(x_value+0.2,x_data)
# 원하는 값으로 대치 되어 진다 위에서 x_data이름으로 적은 배열의 이름이 있다 
plt.legend(loc='upper right')
# 오른쪽 위에 라벨에 정해준 리스트 이름을 띄어 준다 
plt.show()
# 위에서 만들어 준 plt 를 실행 한다