import matplotlib.pyplot as plt
# ass_subplot(특정위치)
# ass_subplot([총 행의 수], [총 열의 수 ],[subplot 번호])

figure = plt.figure()
# figure() 함수 사용해서 figure 에 넣고 
axes1 = figure.add_subplot(2,2,1)
axes2 = figure.add_subplot(2,2,2)
axes3 = figure.add_subplot(2,2,3)
axes4 = figure.add_subplot(2,2,4)
# figure 로 지정된 것을 형태로 add_subplot(2,2,4) 이렇게 
# 추가해주는 프로그램 

axes1.plot([0,1000]) # y 축 데이터
axes2.plot([1,1]) # y 축 데이터
axes3.plot([2,10],[0,10]) # y 축 데이터
axes4.plot([1,0]) # y 축 데이터
# 표시하는 방식을 정해주고 
plt.show()
# 그것을 실제 표시 해주는 것

# subplots() : figure 와 sublplot 동시 생성
# subplots() (생성할 subplots 행 , 열)
figure, axes = plt.subplots(2,2) # subplot 는 두개를 만들어 주는 함수 인데 
# 이함수를 2해 2열 로 표시하면 총 4개를 만들어 준다 
axes[0][0].plot([1,1])
axes[1][1].plot([1,2])
plt.show()

################################
figure = plt.figure()
# figure 객체를 만들어 준다 
axes = figure.add_subplot(224)
# 
x = [ 0, 2, 4, 6]
y = [ 0, 4, 0, 2]
x2 = [ 1,2,3,4,5,6]
y2 = [ 1,2,3,4,5,7]
axes.plot()
# 여기에 
axes.plot(x,y, color='r', linestyle='dashed',marker='^')
axes.plot(x2,y2, color='k', linestyle='dashed',marker='o')
plt.show()
#######################

import matplotlib.pyplot as plt

figure = plt.figure()
axes = figure.add_subplot(111)

x = [1, 2, 3, 4]
y = [1, 4, 3, 2]

x2 = [11, 12, 13, 14]
y2 = [11, 14, 13, 12]

axes.bar(x, y)
axes.bar(x2, y2)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bar Chart')
plt.legend()
plt.show()
################

figure = plt.figure()
axes = figure.add_subplot(111)
x = [10,15,30,20]
y = ['1a','2b','3c','4d']
axes.pie(x, labels=y , autopct='%.1f%%' )
plt.show()

