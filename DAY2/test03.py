# 필요한 라이브러리를 수정할때는 import 를 사용해서 / re 는 다양한 문자열 표현하는 라이브러리
import re 


text = '<title> 지금은 문자열 연습입니다.</title>'
print(text[0:7]) # 변수의 문자열로 0 에서 7까지 출력
print(text.find('문')) # 지정한 문자열의 위치값 리턴 .
print(text.find('파')) # 지정한 문자열에 찾는 글이 없으면 -1 리턴
print(text.index('문')) # 있으면 위치값 리턴
# print(text.index('파')) index 는 없으면 오류값 발생 , 주석처리중

text1 = '     <title> 지금은 문자열 연습입니다.</title>'
print(text1)
print(len(text1)) # 문자열 길이 출력
print(text1.strip()) # 공백 제거 
print(len(text1.strip())) # 공백 제거한 문자열의 길이 출력
print(text1.lstrip())

print(len(text1.lstrip())) # 왼쪽 공백제거 후 길이 출력
print(text1.lstrip()) # 왼쪽 공백 제거

print(len(text1.rstrip())) # 오른쪽 공백제거 후 길이 출력
print(text1.rstrip()) # 오른쪽 공백제거

text2 = ';'
print(text1+text2)
# 문자열 합치기

print(text.replace('<title>','<div>')) # 위치 스왑
print(text.replace('<title>',''))
print(text.upper())
up = text.upper() # 텍스트를 대문자로 변형하면서 up 에 입력
print(up) # 출력
print(up.lower()) # 다시 소문자로 변경 

text3 = '<head>안녕하세요</head>'
body = re.search('<head.*/head>',text3)
# 객체들을 구하는 서치
print(body)
body = body.group()
# 원하는 문자열을 그룹화
print(body)
# import re  정규표현식 re 에 대한 설명
# [0-9] , [a-z]
# ab*c : abc, abbc, abbbbc, abbbbbbc
# *(0번이상) +(1이상) ?(0이상1이하)

print('-----------------------------------------------------------------------')
text4 = ('<head>안녕하세요..<title>지금은 문자열 연습</title></head>')
# <title>지금은 문자열 연습</title> 만 출력하기 정규 표현식에서 
body = re.search('<title.*/title>',text4) # body 에 원하는 title 사이 를 지정하여 
# text4 에 넣게 하는것 그리고 그것을 group() 으로 지정해서 출력해준다 
print(body.group())
# body=re.search('<.+?>', body) 이상태로는 body 는 오브젝만 받아 온것이니 
body=body.group() 
print(body)


# *(0번이상) +(1이상) ?(0이상1이하)
# ? 를 했을때 : 첫번째 애만 지정하는것
body1 = re.search('<.+?>',body)
print('body1 :' , body1.group())
# ? 없이 했을때 
body2 = re.search('<.+>',body)
print('body2 :' , body2.group())
body = re.sub('<.+?>','',body) # 모르는 표현이 있는경우 대체하는걸 지정해준다 
print(body)
