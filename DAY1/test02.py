# 조건문
a = 2
if (a==1) :
    print(1)
else :
    print('1 아님')
    # 중요한건 들여 쓰기 !!!!!!!!!!!

if (a==1) :
    print(1)
elif a==2 :
    print(2)
else :
    print(3)

# 반복문
for i in [1,2,3] :
    print(i) # i 는 1,2,3 
for i in (1,2,3) :
    print(i) # i 는 1,2,3
for i in "Hello" :
    print(i)

num = 5 
while num > 0:
    print(num)
    num -=1

print('-----while------')
# while 문으로 : num 이 6 이면 end 를 출력하고 종료 / 10,9,8
num = 10
while num >= 5 : 
    print(num,end=',')
    num -=1
    if num <= 7 :
        print('end')
        break
    print(num, end = ' ')
    num -= 1


print('='*20)

nums = [1,2,3,4,5]
test = [3,6,7]

for i in nums : 
    if i in test:
        print(i)

print()
print('-------end------')

# 100 까지의 수 중 7 의 배수와 합계 출력

# for 문으로 

sum = 0
for j in range(0,100,7) :
    if j % 7 == 0 :
        print('%d'% j,end=',')
        sum = sum + j
print()
print(sum)

# while 문으로 
j = 0
sum = 0 
#  print('\n ') 는 개행 으로 새줄을 만들어 준다 출력하기 전에 

while j < 100 : # for j in range(101) : 으로도 할수있다
    j += 1
    if j % 7 == 0 :
        sum += j
        print(j , end=',')

print('\n \n%d'%sum)

# * * * 
# * * * 
# * * * 
i,j = 0,0
for i in range(3) :
    for j in range(3) : 
        print('*',end=' ')
    print()

# 딕 정리 

d1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
max = max(d1.values())
print("최대값 : ", max)
print(d1.items()) # key 와 item 을 한번에 출력 
for k,v in d1.items() : # k 에 key , v 에 value 넣는데 ,d1의 item 값을 k 와 v 에 입력한다 
    # 최대 벨류의 키값 출력하기 
    print('key : ', k ,'value : ',v)
    if v == max:    # () 하든 안하든 상관 없음 
        print(k)  