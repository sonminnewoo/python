import re

text = "<title>지금은 문자열 연습입니다.</title>"
print(text[0:7])
print(text.find('문'))   #  있으면 위치값 리턴
print(text.find('파'))   #  없으면 -1 리턴
print(text.index('문'))  #  있으면 위치값 리턴
# print(text.index('파'))  #  없으면 오류발생

text1 = "      <title>지금은 문자열 연습입니다.</title>     "
print(text1)
print(len(text1))
print(text1.strip())
print(len(text1.strip()))
print(text1.lstrip())
print(len(text1.lstrip()))
print(text1.rstrip())
print(len(text1.rstrip()))
text2 = ";"
print(text1+text2)

print(text.replace('<title>', '<div>'))
print(text.replace('<title>', ''))
up = text.upper()
print(up)
print(up.lower())

text3 = "<head>안녕하세요</head>"
body = re.search('<head.*/head>', text3)
print(body)
body = body.group()
print(body)
# [0-9],[a-z]
# ab*c : abc, abbc, abbbbc, abbbbbbc
# *(0번이상) +(1이상) ?(0이상1이하)

print("--------------")
text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
body = re.search('<title.*/title>', text4)
body = body.group()
print(body)
body1 = re.search('<.+?>', body)
print('body1 :' , body1.group())
body2 = re.search('<.+>', body)
print('body2 :' ,body2.group())
body = re.sub('<.+?>', '', body)
print(body)


