import numpy as np  # as 해서 닉네임을 만들어 버리고 , numpy 을 import 했다
# 아나콘다가 설치 안되어있으면 pip install 해줘야 한다 
a = np.array([[2,3],[5,2]]) # 2차원 배영
print(a)
d = np.array([2,3,4,5,6]) # 1차원 배열 만들고 
print(d)
print(d.shape)
e = np.array([[1,2,3,4],[3,4,5,6]])
print(e.shape) # 리스트 형태를 출력
print(e.dtype) # int 형태
print(np.zeros((2,10)))
print(np.ones((2,10)))
print(np.arange(2,10)) # 2 이상 10 미만의 원소로 이루어진 1차원 배열

# 1로 이루어진 2행 3열의 a 해열을 생성

a = np.ones((3,2))
print(a)
b = np.transpose # 행과 열이 바뀜
print(b)

arr1 = np.array([[2,3,4],[6,7,8]])
arr21 = np.array([[12,13,14],[26,27,28]])
print(arr1+arr21) # 배열 덧샘 ==> 같은 자리의 원소끼리 덧셈 
print(arr1-arr21)
print(arr1/arr21)
print(arr1*arr21)
########################################################
# d = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,7,8,9,9]])
print("-----------------------------------------------------")
d_list = [[1,2,3,4,5],[2,3,4,5,6],[5,6,7,8,9,9]]
minwoo_list = [[1,2,3,4,5],[2,3,4,5,6],[5,6,7,8,9,9]]
print("-----------------------------------------------------")
d = np.array([[1,2,3,4,5],[2,3,4,5,6],[5,6,7,8,9]])
print(type(d_list))
print(d_list)
print(minwoo_list)
# 그냥 _list 하는것 만으로 np.array 한 기능을 할수 있다 .
print(d_list[:2])
# d_list[:2] = 0 오류 발생  [:2] 로 ~ 에서 ~ 까지 의 리스트 의 값을 지정하는것 
# 안된다
d_list[2] = 0
print(d_list) 
# 특정 항목은 수정이 가능하다 
print('==============================================')
d[:2] = 0  # 이런식으로 배열은 수정할수 있다 , 리스트는 안된다!!! 
#  차이는 d[:2] '배열' 과 d_list[:2] 라는 리스트의 지정 의 차이 이다.
print(d)
print(np.arange(10))
arr4 = np.arange(10)+1 # 각 원소에 1 씩 더해주는 것 
print(arr4)
print(arr4[:5]) # 5 개 까지 출력 
print(arr4[-3:]) # 마지막 에서 3 개 출력