import numpy as np
SIZE = 5
startRow, startCol = 1,1
nSIZE = 3

value = 1
myAry1 = np.arange(value, value+(SIZE*SIZE),1)
print(myAry1)
myAry1 = myAry1.reshape(SIZE,SIZE)
print(myAry1)

for i in range(SIZE):
  [ print("%3d" %myAry1[i][k] , end =' ') for k in range(SIZE) ]
  print()
print('------') 

for i in range(SIZE):
  for k in range(SIZE):
    print("%3d" %myAry1[i][k] , end =' ')
  print()

## 넘파이 2차원 배열의 슬라이싱  
myAry2 = myAry1[startRow:startRow+nSIZE , startCol:startCol+nSIZE]
print(myAry2)
myAry3 = myAry1[startRow:startRow+nSIZE , startCol:startCol+nSIZE].copy()
print(myAry3)