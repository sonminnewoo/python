import pandas as pd
import numpy as np

data1 = np.arange(9).reshape((3,3))
# 1차원 배열 만들고 , 2차원 3행 3열
data2 = np.arange(12).reshape((4,3))
print(data1)
print(data2)

df1 = pd.DataFrame(data1,columns=list('가나다') , index=['서울','부산','광주'])
df2 = pd.DataFrame(data2,columns=list('가나다') , index=['고양','서울','광주','대전'])
print(df1)
print(df2)
newDf = df1 + df2
# 데이터 프레임도 더하기가 된다
print(newDf)
