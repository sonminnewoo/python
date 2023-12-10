import numpy as np

# 넘파이 2차원 배열 생성
SIZE = 5
numpyAry = np.random.randint(0,255, size=(SIZE, SIZE))
print(numpyAry)
numpyAry +=100  # 배열에 각 원소에 100더하기
print(numpyAry)

