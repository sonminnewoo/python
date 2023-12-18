import matplotlib.pyplot as plt
# 그래프 표시! 

x = [1, 4, 9, 16, 25, 36, 49, 64]

# plt.plot(x)
# plt.show()

y = [i for i in range(1,9)]
#print(y)
plt.xlabel('x')
plt.ylabel('y')
# 해당하는 기준축 에 x, y 라는 글을 입력하는 것 
plt.title('matplotlib sample')
plt.plot(x,y)
# plt 라이브러리 에 , plot 에 x,y 값을 넣고 
# plt.show()
# plt 에 넣은것을 사용하는것 

y1 = [13, 16, 15, 18 ,16 , 17, 16]
y2 = [i for i in range(1,9)]
plt.plot(y1,y2)
plt.show()

# 이렇게 위에있는 plt.show() 를 지우고 맨 마지막에 show 를 해주면 작성해줬던 내용이 다 
# 그래프로 표시된다 

############################################
import numpy as np
points = np.array([[1,1], [2,2],[3,3],[4,4],[5,5]])
print(points)
# 리스트 출력
print(points.shape)
# list 형태를 확인
plt.plot(points[:,0],points[:,0]) # [:] 만 되면 모든 좌료 의미 , [:,0]) 모든 열에서 첫번째 열을 의미
# 그래프를 일단 0에서 시작하게 하는 것
plt.show()
