# 89페이지
# 반복문 으로 간략하게 할것 
money = 0
money = int(input("교환할 돈은 얼마?"))
don = [500,100,50,10] # 이걸 지칭하기위해 i

# 반복문 for

for i in don : # for : for '변수' in range(시작값,끝값+1,증가값) : 
                            # 이 부분을 반복
    print("%d원 짜리 ==> %d개" % (i,int(money//i)))
    money %= i
print("바꾸지못한 돈은 %d원" %money)

# print("\n 500원 짜리 ==> %d 개" % int(money//don[0])) 
# money %= don[0]