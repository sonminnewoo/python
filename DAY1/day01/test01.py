print('Hello')
a = 0
print(a)
print(type(a))
b= 'Hello World'
print(b)
print(type(b))
c="'안녕하세요'"
print(c)
d = "\'안녕하세요\'"
print(d)
print(b+c)
print(2*3)
print('2'*3)
print(c*3)
print("="*10)
print(b)
print(b[0])
print(b[-1])
e= '안녕하세요'
print(e[0:2])
print(e[1:3])
print(e[0:5:2])
print(e[:])
#list
l = list()
print(l, type(l))
lst = [1,2,3]
print(lst, type(lst))
l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(l, type(l))
# l 의 첫번째 값 출력
print(l[0])
# l 의 길이 출력
print(len(l))
# l 리스트의 마지막 값 출력 
print('마지막 : ', l[-1])
# l 리스트의 마지막 값 출력 len 이용
print('마지막  len 이용: ', l[len(l)-1])
# l 리스트의 첫번째 값을 99 수정
l[0] = 99
print(l)
l[1] = [1,2,3]
print(l)
l[2] = '문자'
print(l)
l.append(9999)
print(l)
l.remove(5)
print(l)

# tuple
t = tuple()
print(t, type(t))
t1 = (1,2,3)
print(t1, type(t1))
print(t1[0], t1[0:2])
print(t1+t1)
# t1[0] = 5 오류발생 수정 안됨
print(t1)

#  dict
d1 = dict()
print(d1, type(d1))
d = {
  'a' : 1,
  'b' : 2,
  'c' : 3,
  'd' : 3
}
print(d, type(d))
print(d['a'])
d['b'] = 33
print(d)
# print(d['d']) 오류발생
d1 = d.keys
print("d1" , d1)
d2 = d.values
print("d2" , d2)
d3 = d.items
print("d3" , d3)
######
d11 = d.keys()
print("keys" , d11)
print("type d11" , type(d11))
d22 = d.values()
print("values" , d22)
print("type d22" , type(d22))
d33 = d.items()
print("items" , d33)
print("type d33" , type(d33))

print("type list : " , type(list(d.keys())))
print("type list : " , type(list(d.values())))
print("values : " , d.values() )
print("values set : " , set(d.values()) )
