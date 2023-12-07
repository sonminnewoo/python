money = 0
money = int(input("교환할 돈은 얼마 ? "))  # 321
don = [500,100,50,10]

print("\n 500원짜리 ===> %d개 " % int(money // don[0]) )
money %= don[0]
print(" 100원짜리   ==> %d개 " % int(money // don[1]) )
money %= don[1]
print(" 50원짜리 ==> %d개 " % int(money // don[2]) )
money %= don[2]
print(" 10원짜리   ==> %d개 " % int(money // don[3]) )
money %= don[3]
print(" 바꾸지 못한 잔돈 ==> %d원" % money)