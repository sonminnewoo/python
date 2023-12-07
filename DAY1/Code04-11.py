def func1():
    a= 10 # 지역변수 
    print(a)


def func2():
    print(a)

a = 20 # 전역 변수 
func1() # 지역변수 a

func2() # 전역변수 a