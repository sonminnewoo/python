import numpy as np

# 넘파이 2차원 배열 생성
SIZE = 5
numpyAry = np.random.randint(0,255, size=(SIZE, SIZE))
# numpyAry 라는 변수에 난수 발생.정수로 .
print(numpyAry)
numpyAry +=100 # 배열에 100 더하기
print(numpyAry)