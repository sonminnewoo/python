a = int (input("숫자를 입력하세요 : "))
b = int (input("숫자를 입력하세요 : "))
# a = input()이렇게 하고 계산을 하면 오류 가 발생한다 
#  문자열을 계산했기 때문 

result = a+ b
# 이렇게 계산하면 오류가 난다
# 문자열로 받기 때문이다 문자는 계산할수 없기 때문 

print(a, "+", b, "=", result)
# 이렇게 출력하면
result = a* b
print(a, "*", b, "=", result)