def seperate():
  a = int(input('수 입력'))
  if a % 2==0 :
    print("짝수")
  else :
    print("홀수") 

# 덧셈
def addReturn(a, b):
  return a+b     


# seperate()
sum  = addReturn(3,5)
print("addReturn 결과 : ", sum)
print("addReturn 결과1 : ", addReturn(13,15))

# 1부터 num까지의 합을 계산하는  hap  함수 정의
def hap(num):
  h = 0
  for i in range(1,num+1):
    h += i
  return h

print(hap(10))
print(hap(100))