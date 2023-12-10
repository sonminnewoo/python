import re #문자열에 관련된 것들을 좀 더 다양하게 사용할 수있는 라이브러리
text = "<title>지금은 문자열 연습입니다.</title>"
print(text[0:7])
#문의 위치값을 출력하고 싶다. 
print(text.find('문'))
print(text.find('파'))#파인드느 ㄴ없으면 -1리턴
print(text.index('문'))
# print(text.index('파'))# 없으면 오류발생 인덱스

text1 = "    <title>지금은 문자열 연습입니다.</title>    "
print(text1)
print(len(text1))
print(text1.strip())
#print(text1.lstrip())
print(len(text1.rstrip()))
text2 ="dfkdl"
print(text1+text2)
print(text.replace('<title>', '<div>'))
up = text.upper()
print(up)
print(up.lower())
text3 = "<head>안녕하세요</head>"
body = re.search('<head.*/head>', text3)
print(body)
body = body.group()
print(body)
#[0-9], [a-z]
#ab*c : abc, abbc, abbbbc, abbbbbc]
#별은 0번이상 더하기는 1이상 물음표는 0이상 1이하

print("-------------------")
text4 = ('<head>안녕하세요...<title>지금은 문저ㅏ열 연습</title></head>')

body = re.search('<title.*/title>', text4)
body = body.group()
print(body)
body1 = re.search('<.+?>', body)
print('body1 :' , body1.group())
body2 = re.search('<.+>', body)
print('body2 :',body2.group())
body = re.sub('<.+?>', ' ', body)
