money = 0
money = int(input("교환할 돈은 얼마 ? "))  # 321
don = [500,100,50,10]

for i in don:
    print("%d원짜리 ===> %d개 " % (i, int(money // i)) )
    money %= i
print("바꾸지 못한 잔돈 ==> %d원" % money)
