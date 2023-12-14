import numpy as np
import matplotlib.pyplot as plt
SIZE = 30 # 표시 갯수 

x_value = np.random.rand(SIZE)
y_value = np.random.rand(SIZE)
sizeAry = (50 * np.random.rand(SIZE)) ** 2
# 랜덤하게 사이즈를 지정
colorAry = np.random.rand(SIZE)
# 랜덤하게 색상을 지정 

plt.scatter(x_value,y_value ,s=sizeAry, c=colorAry, alpha=0.5 , cmap='summer')
# 색상 구성 spring(),summer(),autumn() , winter()
# scatter 값에 따라 표에 표시하는 그래프 표시
plt.colorbar()
plt.show()