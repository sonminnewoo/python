import numpy as np

pList1 = [10,20,30,40]
pList2 = [10,20,30,40.0]

numpyAry1 = np.array(pList1)
print(numpyAry1, numpyAry1.dtype)

numpyAry1 = np.array(pList2)
print(numpyAry1, numpyAry1.dtype)

numpyAry2 = np.array(pList1, dtype=np.float32)
print(numpyAry2, numpyAry2.dtype)

numpyAry3 = np.arange(5)
print(numpyAry3, numpyAry3.dtype)

numpyAry4 = np.ones(5)
print(numpyAry4, numpyAry4.dtype)

numpyAry44 = np.zeros(5)
print(numpyAry44, numpyAry44.dtype)

numpyAry5 = np.ones(5, dtype=np.uint16)
print(numpyAry5, numpyAry5.dtype)
#  위의numpyAry5 를 실수 float 형태로 바꿔주는 numpyAry6 
numpyAry6 = numpyAry5.astype(np.float16)
print(numpyAry6, numpyAry6.dtype)

