# print("안녕하세요?")
# print("안녕하세요?")
# print("안녕하세요?")
# print("안녕하세요?")
# print("안녕하세요?")

# for 문 사용
# for i  in range(0,5): 
#   print("%d 안녕하세요?" % i)

# for 문 사용 1에서 10까지의 합  
hap = 0
for i in range(1,11):
  hap += i  # hap = hap + i
print("1부터 10까지의 합계 : %d " % hap)  

# 1에서 10까지의 짝수 합 출력
sum = 0
for i in range(1, 11):
  if i % 2 ==0 :
    sum = sum + i
print(sum)  

# 1에서 10까지의 홀수 합 출력
h = 0
for i in range(1, 11, 2):
  h += i
print(h)

# 구구단 출력
for i in range(2, 10, 1):
  print("%d단 "  % i)
  for j in range(1, 10):
    print("%d * %d = %d" %(i, j, i*j))
    












