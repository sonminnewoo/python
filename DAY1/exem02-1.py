# 89페이지
# 02 에서 쓸모없는걸 지움
money = 0
money = int(input("교환할 돈은 얼마?"))
# don = [] 이거를 리스트라고 생각한다 
don = [500,100,50,10] # 리스트 를 활용해서 계산하는걸 보여주기 위해 'don'리스트 추가

# print("\n 500원 짜리 ==> %d " % money //500)
# 이대로 실행하면 print("\n 500원 짜리 ==> %d " % money  이게 문자로 취급되어 진다 
print("\n 500원 짜리 ==> %d " % int(money//500)) # 이런식으로 바꾸고
# print("\n 500원 짜리 ==> %d " % int(money//don[0]) 이런식으로 리스트를 활용해서 이용할수도 있다. 
# 이렇게 하면 don 리스트로 값을 지정할수 있다 

money %=500 # 위 를 사용해서 계산하면서 출력하더라도 money 를 계속 갱신은 해야하니 이걸 추가한다
print("\n 100원 짜리 ==> %d " % int(money//100))
money %=100
print("\n 50원 짜리 ==> %d " % int(money//50 ))
money %=50
print("\n 10원 짜리 ==> %d " % int(money//10))
money %=10 
print("\n 바꾸지 못한 잔돈 ==> %d " % int(money))