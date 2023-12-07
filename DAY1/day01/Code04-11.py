def func1():
  a = 10  # 지역변수
  print(a)

def func2():
  print(a)

a = 20 # 전역변수
func1()
func2()