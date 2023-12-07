# 128 페이지 / chapter 4 전부  

print('Hello')
a = 0
print(a) # print는 a 를 출력하지만
print(type(a)) # print(type(a)) 는 a 의 타입을 출력한다
b = 'Hello World'
print(b)
print(type(b))
c="'안녕하세요'"
print(c)
d = "\'안녕하세요\'"
print(d)
print(b+c)
print(2*3)
print('2' *3)
# 이렇게 문자뒤에 *3 하면 3번 반복 출력하게 된다
print(c*3)
# 이렇게 변수는 어차피 그자체 이니 출력하는 횟수만 *3 으로 해주면 된다
print('='*10)
print(b)
print(b[0])
print(b[-2])
# [] 안에 '-' 붙으면 끝에서 부터 순서 의미 
e='안녕하세요'
print(e[0:2])
print(e[1:3])
print(e[0:5:2])
print(e[:])

#list ---------------------------------------------------------------
print("list ---------------------------------------------------------------")

l = list() 
print(1,type(1))
lst = [1,2,3]
print(lst,type(lst))
l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(l,type(1))
# l의 첫번째 값 출력
print(l[0])

# l의 길이 출력
print(len(l))

# l리스트의 마지막 값 출력

print(l[-1])
# l리스트의 마지막 값 출력,len
print(l[len(l)-1])
l[0] = 99
print(l)
l[1] = [1,2,3]
print(l)
#  리스트 안에 리스트 넣는것 , 가능
l[2] = '문자'
print(l)
l.append(9999)
# 끝에 항목 추가 및 값지정
print(l)
l.remove(99)
# 끝에 항목 제거 / 값으로 지정 
print(l)

print("-------------------------------------------------------------")

# tuple : 괄호 안에 리스트를 만들어 준다 
t=tuple()
print(t,type(t))
t1 = (1,2,3)
print(t1,type(t1))
print(t1[0],t1[0:2])
print(t1+t1)
# t1[0] = 5 tuple 로 만든건 리스트를 만들수 있지만 안에 자료를 수정할수는 없다
print(t1)

# dict : 중괄호로 만들어 준다 , hash map : p와 value 로 구성
# 목차
print('구분1')
d = dict()
print('구분2')
print(d,type(d))
print('구분3')
d = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'c' : 33, # keys 는 중복을 허용하지 않는다  
    'd' : 2 # value 는 중복을 하용한다 
}
print('구분4')
# 1,2,3 각 a,b,c 
print(d, type(d))
print('구분5') 
print(d['a']) # 이걸 출력하면 목차를 반환 해준다
print('구분6')
d['c' ] = 33
print('구분7')
# c 라는 것의 목차를 33 으로 변경 , 목차를 지정한것임 그걸 출력하면 목차값을 출력할것이고
print(d)
print('구분8')
# print(d['d']) 오류발생 , d 라는 리스트에 d 라는 값을 가진 목차가 없기 때문 
d1 = d.keys
print("d1",d1)
d2 = d.values
print("d2",d2)
d3 = d.items
print("d3",d3)
########################
d11 = d.keys()
print("keys", d11)
print("d11", type(d11))
d22 = d.values()
print("values" ,d22)
print("type d22", type(d22))
d33 = d.items()
print("items", d33)
print("type d33", type(d33))

print('구분1')
print("type list : ", type(d.keys)) # 형변환 
print("type list : ", type(list(d.keys()))) # 문자를 int 로 바꾸듯 형변환
    #  이렇게 key를 리스트로 형변환 해준다  
print("type list : ", type(list(d.values())))
print("values : ", d.values())
print("values set : ", set(d.values()))
#  java 처럼 중복을 허용하지 않게 set 으로 고정 해준다 
# 객체를 생성하는 방법으로 파이썬에서는 리스트, 투쁠, 