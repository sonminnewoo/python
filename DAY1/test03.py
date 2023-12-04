def seperate() : # 자바 void public 이라는 것처럼 
    a = int(input('수 입력'))
    if a % 2==0 :
        print('짝수')
    else : 
        print('홀수')
    print(a)

def addReturn(a,b) :
    print('함수')
    print(a)
    print(b)
    print(a+b)
    return a+b

# seperate()
sum = addReturn(3,5)
print("addReturn 결과 : ",sum)
print("addReturn 결과1 : ",addReturn(13,15))
# 자바에서는 리턴 을하거나 , 리턴이 없으면 void 로 함수형을 만들어서 출력 문으로 변수를 출력하는데 , 여기는 
# 그런게 없기 때문에
# 함수에서 어떤 대상에 대입하기 위해서는 rerurn 을 써서 지정 해준다 

# 여기서는 매개변수를 받아 오는데 

#  아래 선언하는곳에서는 지정안하면 오류

# 1 에서 10 까지 합을 계산하는 hap 함수 정의

def hap (s) :
    sum = 0
    for h in range(1,s+1) : # 1 부터 s 까지 하려면 s+1 해야 실제 s 만큼 계산한다
        sum += h  # 1+10  2+10  3+13
    return sum 
# 돌려주는 값이있으면 java 는 'return' 이나 'void' 로 해서 출력문으로 
# 반환 하지만 이건 함수에 'return' 을 해줘야한다

print(hap(10))
print(hap(100))