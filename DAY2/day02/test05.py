import codecs
import re

f = codecs.open('friends101.txt','r',encoding='utf-8')
script101 = f.read()

print(script101[:100])
#  Monica: 
Line =re.findall(r'Monica:.+', script101)
print(Line)
print(Line[:3])
print(type(Line))
# All: 대사 출력
All =re.findall(r'All:.+', script101)
print(All)
# All의 마지막 대사
print(All[-1])
print(len(All))
print('================')
# 출연진 만 출력
char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char,script101 ))

###################
a = [1, 2, 3, 4, 5, 2, 2]
print(a)
print(set(a))
# print(set(re.findall(char,script101 )))
y = set(re.findall(char,script101 ))
print(type(y))
lst = list(y)
print(type(lst))
print(lst)
#  : 빼고 출연진만 출력
character = []
for i in lst:
  character += [i[:-1]]
character.sort()  
print('출연진 : ', character) 
print(len(character)) 

print("*****************")

character2 = []
for i in lst:
  ch = re.sub(':','',i)
  character2.append(ch)
character2.sort()  
print(character2)
print(len(character2))  
print()
print()
# 지문만 추출하는데 처음부터 6개만 출력
# (The Pilot-The Uncut Version) 
txt1 = re.findall(r'\([A-Za-z].+[a-z|\.]\)', script101)[:6]
print("txt1 >>>\n" , txt1)
print()
txt2 = re.findall(r'\([A-Za-z].+\.\)', script101)[:6]
print("txt2 >>>\n" , txt2)
###################
a = '제 이메일 주소는  greate@naver.com'
a += ' 오늘은  today@naver.com 내일은 apple@gmail.com  life@abc.co.kr 라는 메일을 사용합니다.'
print(a)
# 메일 주소만 출력
a1 = re.findall(r'[a-z]+@[a-z.]+', a)
print(a1)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
# a로 시작하는 단어 출력
alist = []
for i in words:
  alist += re.findall(r'a[a-z]+', i)
print ('alist  : ' , alist) 

for i in words:
  blist = re.search(r'a[a-z]+', i)
  if blist : 
    print(blist.group())   # blist  생성되지 않은 상태에서 group() 사용해서 오류

print()
for i in words:
  # m = re.match(r'a[a-z]+', i)  # pattern 을 문자열의 첫부분과 비교
  m = re.match(r'a\D+', i)  # \d(숫자) \D(숫자 아닌)
  if m:
    print(m.group())





  









