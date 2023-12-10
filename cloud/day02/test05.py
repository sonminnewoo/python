import codecs
import re
f = codecs.open('friends101.txt', 'r', encoding= 'utf-8')
script101 = f.read()

print(script101[:100])
#Monica:
Line = re.findall(r'Monica:.+', script101)
print(Line)
print(Line[:3])
print(type(Line))
#All: 대사출력
L = re.findall(r'All:.+', script101)
print(L)
#마지막 대사구하라
print(L[-1])
print(len(L))
print("=======================")
#출연진만 출력
char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))


################################
a = [1,2,3,4,5,2,2]
print(a)
print(set(a))
print(set(re.findall(char, script101)))
y = set(re.findall(char, script101))
print (type(y))
lst = list(y)
print(type(lst))

character = []
for i in lst:
    character +=[i[:-1]] 
print('출연진 : ', character)

character2 = []
for i in lst:
    
    character2.append(re.sub(':', '', i))
print(character2)

character.sort()
print('출연진 : ', character)
print(len(character))
#지문만 추출하는데 처음부터 6개만 출력
#(The Pilot-The Uncut Version)
# s = re.compile(r'([A-Za-z].+[a-z.])')
# print(set(re.findall(s,script101)))
# print(s)

# s2 = re.compile(r'([A-Za-z].+[a-z.])')
# print(set(re.findall(s2,script101)))
# print(s2)

#메일주소만 출력
a = '제 이메일 주소는 greate@naver.com'
a += '오늘은 today@naver.com 내일은 apple@gmail.com life@abc.co.kr 라는 이메일을 사용합니다.'
print (a)
#메일주소만 출력
mail = re.findall(r'[a-z]+@[a-z.]+', a)
print(mail)

words = ['apple','cat','brave','drama','arise','blow','coat','above']
#a로 시작하는 단어 출력
alist = []
for i in words:
    alist += re.findall(r'a[a-z]+', i)
print('alist :', alist)
for i in words:
    blist = re.search(r'a[a-z]+', i)
    if blist:
     print(blist.group()) #blist 생성되지 않은 상태에서 group() 사용해서 오류
print()
for i in words:
    # m = re.match(r'a[a-z]+', i)
    m = re.match(r'a\D+', i)
    if m:
        print(m.group())
        #match는 시작위치에서 찾는다. 패턴을 문자열의 첫부분과 비교
