# 91 페이지
a = int(input("값을 입력하세요"))

if a < 100 : 
    # 조건이 참이면 
    print("100보다 작군요")
    print("거짓이므로 이 문장은 안보이겠죠?")
else :
    print("100보다 크네요")

# if a % 2 : 
#     # 조건이 참이면 
#     print("홀수 이네요")
# else :
#     print("짝수이네요")

# 위를 다른 방법으로 구현 하려면 아래처럼 

str = "" # 출력문을 변수 에 담으면 닶을 여러개 써야할때 유용
if a % 2 == 0 :
    str = "짝수"
else : 
    str = "홀수"
print("%d %s" %(a,str))

# 조건이 거짓이면
print("프로그램 끝") 