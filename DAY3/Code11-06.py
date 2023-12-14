import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
inFilename = './python/cloud/Excel/singer.xlsx'
outFilename = './python/cloud/Excel/singer_out.xlsx'

df_seniro = pd.read_excel(inFilename, 'senior',index_col=None)
df_junior = pd.read_excel(inFilename, 'junior',index_col=None)

df_seniro = pd.read_excel(inFilename, 'senior',index_col=None)
df_singer = pd.concat([df_seniro,df_junior])
#print(df_singer)
#인원이 6명 이상인 팀

print()
df_singer_over6 = df_singer[df_singer['인원']>=6] # 인원이 6보다 큰것
print(df_singer_over6)

df_singer_over6 = df_singer_over6.sort_values(by=['인원'], axis=0,ascending=False)
# ascending=False 내림차순 정렬 True 오름차순 정렬 , 정렬 기준축 axis=0 열기준
# 1 행기준 , sort_values 값으로 정렬한다 , by=['인원'] '인원'으로 df_singer_over6
# 을 df_singer_over6 로 
print(df_singer_over6)
#    아이디    이름  인원  주소  평균 키       데뷔 일자  유튜브 조회수
# '아이디','이름','인원','유튜브 조회수' 만 출력하게 하는것 loc 
df_singer_over6 = df_singer_over6.loc[:,['아이디','이름','인원','유튜브 조회수']]
# loc 원하는 열을 선택해서 하는 함수
# 원하는걸 출력하기 위해!!!! 원하는 열 !! 열!! 
print(df_singer_over6)

# 각 팀별 인원 수를 막대그래프
x_data = df_singer_over6['아이디']
y_data = df_singer_over6['인원']
colorAry = [np.random.choice(['red','green','blue','brown','gold','lime','aqua','magenta','purple']) 
            for _ in range(len(x_data))]
plt.bar(x_data,y_data,color=colorAry)
plt.show()

# 파일로 출력
writer = pd.ExcelWriter(outFilename)
df_singer_over6.to_excel(writer,sheet_name='singer', index=False)
# writer.save() 버전업 되면서 save 대신 close 사용
writer.close()
print('Save, ok~')