import numpy as np
a = np.array([[2,3], [5,2]])
print(a)
d = np.array([2,3,4,5,6])
print(d)
print(d.shape)
e = np.array([[1,2,3,4],[3,4,5,6]])
print(e.shape)
print(e.dtype)
print(np.zeros((2,10)))
print(np.ones((2,10)))
print(np.arange(2,10)) # 2이상 10 미만의 원소로 1차원배열을 만들어주는 함수
# 1로 이루어진 2행 3열의 a 배열을 생성
# pip install
a = np.ones((2,3))
print (a)
b = np.transpose(a) #행과 열이 바뀜
print(b)
arr1 = np.array([[12,13,14], [26,27,28]])
print(arr1+arr2)
#########
# d = np.array([[1,2,3,4,5], [2,3,4,5,6,7],[5,6,7,8,9,9]])
d = np.array([[1,2,3,4,5], [2,3,4,5,6],[5,6,7,8,9]])
d_list =np.array([[1,2,3,4,5], [2,3,4,5,6,7],[5,6,7,8,9,9]])
print(d_list)
print(type(d_list))
print(d_list[:2])
# d_list[:2] = 0 ==>error
d_list[2] = 0
print(d_list)

print('=======')
d[:2] = 0
print(d)
print(np.arange(10))
arr4 = np.arange(10)+1 #각 원소에 +1 : 마치 포문을 돌린거와 같은 역할을 해준다
print(arr4)
print(arr4[:5])
print(arr4[-3:])