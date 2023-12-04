# 101 페이지

for num in range(0,5) : 
    # range(0,5) 0 에서 5라고 지정하지만 , range(10,15) : 해도 반복횟수는 같고 
    # 변수 num 이 10에서 15로 된다 
    print("%d 안녕하세요" % num)
    # 변수 지정이 아마 순서대로 될것임 %d 는 자료의 형식 , % 대상
    print(len("안녕하세요?"))
    # "안녕하세요?" 길이를 출력 
for num2 in range(0,10,3) :
    # range(0,10,3) 이렇게 지정하면 0에서 10 까지 3씩 증가한다.
    print("%d"%num2)

# for 문 사용 1에서 10까지 합
# 짝수일때만 더해서 출력 하기 / sum
sum = 0 # 0 으로 초기화 해준다
for d in range(1,11) :
    # range(1,11,2) : 이렇게 증가할수도 있다 
    if d % 2 ==0 : 
        sum += d
        # 들여 쓰기 조심!!

print(sum)
print("1부터 10까지 합계%d"% sum)

# ---------------------------구구단 출력하기----------------------------

for f in range(2,9) :
    print("%d 단"%f)
    for f2 in range(1,9) : 
        print("%d * %d = %d "% (f,f2,f*f2))
    print("")
    