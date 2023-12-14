import numpy as np

SIZE = 5
startRow, startCol = 1,1
nSIZE = 3

value = 1
myAry1 = np.arange(value, value+(SIZE*SIZE),1)
# np.arange(시작 , 끝 , 증분)
print(myAry1)
myAry1 = myAry1.reshape(SIZE,SIZE)
# myAry1 = myAry1.reshape(SIZE,SIZE)
# myAry1 을 myAry1 자신 의 형태를 reshape(SIZE,SIZE) 지정한 값의 열과 행으로 바꾼다
print(myAry1)

for i in range(SIZE):
    [ print('%3d' %myAry1[i][k], end=' ')  for k in range(SIZE)]
    print()
print('--------------------------------')

for i in range(SIZE):
    for k in range(SIZE):
        print('%3d' %myAry1[i][k], end=' ') 
    print()

## 넘파이 2차원배열 의 슬라이싱
myAry2 = myAry1[startRow:startRow+nSIZE , startCol:startCol+nSIZE]
print(myAry2)

myAry3 = myAry1[startRow:startRow+nSIZE , startCol:startCol+nSIZE].copy()
print(myAry3)