a = int(input("수 입력 : "))

# 수를 입력 받아 그 수가 짝수인지 홀수 인지 출력
str =""
if a % 2 == 0 :
  str = "짝수"
else :
  str = "홀수"

print ("%d %s" % (a, str))  


