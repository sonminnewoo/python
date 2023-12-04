# 조건문
a = 2
if (a==1):
  print(1)
else :
  print('1 아님')  

if (a==1):
  print(1)
elif a==2 : 
  print(2)  
else :
  print(3)    

# 반복문 
for i  in  [1,2,3]:
  print(i)

for i in (1,2,3):
  print(i)

for i in "Hello":
  print(i)

num = 5
while num > 0:
  print(num)
  num -= 1

print('--while---') 
# num 이 6이면 end 를 출력하고 종료   : 10 9 8 7 ---end---
num = 10
while num > 0 :
  if num == 6 :
    print('---end---')
    break
  print(num, end = ' ')
  num -= 1 
print('='*20)

nums = [1,2,3,4,5]  
test = (3,6,7)
for i in nums:
  if i in test:
    print(i)
# 100  까지의 수 중 7의 배수와 합계 출력
sum = 0
for i in range(101):
  if i % 7 ==0 :
    sum += i
    print(i ,end =' ')
print("\nsum : " , sum)    

# * * *
# * * *
# * * *

for i in range(3) :
  for j in range(3):
    print('*', end='')
  print()

d1 = {
    'a': 1,
    'b': 2,
    'c': 3
} 
max = max(d1.values())
print("최대값 : ",max ) 
print(d1.items()) 
for  k, v  in d1.items():
  print('key : ',  k , 'value : ', v )
  # 최대 value의 키값 출력
  if v == max:
    print(k)

