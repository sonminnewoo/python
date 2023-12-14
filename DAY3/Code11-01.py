import pandas as pd # pip install pandas 아나콘다 설치 안되어 있으면 이렇게 작성 해줘야 한다

sr1 = pd.Series([10,20,30,40], index=['다현','정현','쯔위','사나'])
sr2 = pd.Series([50,60,70,80], index=['다현','정현','쯔위','사나'])
sr3 = pd.Series([11,22,33,44], index=['다현','정현','쯔위','사나'])
# print(sr1)
sr12 = sr1 + sr2
print(sr12, '\n')
sr13 = sr1 + sr3
print(sr13, '\n')