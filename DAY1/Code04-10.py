def calc(v1, v2, op) : # v1 = 10 , v2 = 20 , op = +
    result = 0   # 지역변수
    if op=='+' :
       result = v1+v2
    elif op=='-' :
        result = v1-v2
    elif op=='*' :
        result = v1*v2
    elif op =='/' :
        result = v1/v2
    return result

# 이부분을 java 에서는 반드시 지정해줘야하지만
# 파이썬은 ★ 한곳 에 서 = 한거로 바로 초기 값이 지정되게끔 유연하다
res = 0
var1,var2,oper  = 0,0,""
# ★ 
oper = input("계산을 입력하세요(+, -,* , /) : ") # +
var1 = int(input("첫 번째 수를 입력하세요 : ")) # 10
var2 = int(input("두 번째 수를 입력하세요 : ")) # 20

res = calc(var1, var2, oper)
# 함수로 값을 반환하려면 이렇게 함수안에 return 도 있어야하고 
# 바로 출력 할수 없으니 반환하는걸 변수에 넣어서 
# 출력 문 으로 지정해주면 최종 출력 한다
print(res)
print("## 계산기 : %d%s%d = %d" % (var1,oper,var2,res))