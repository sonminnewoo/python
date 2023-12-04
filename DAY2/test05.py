import codecs # 파일 열기 
import re # 객체 확인 

f = codecs.open('friends101.txt','r', encoding='utf-8')
script101 = f.read()

print(script101[:100]) # 처음부터 100 까지
# Monica: 라는 글자만 읽어 오는것 
# Line = re.findall(r'Monica : ', script101) #script101 이라는 것에서 정규표현 'findall'로 
# . 은 문자를 의미 
Line = re.findall(r'Monica:.+', script101) # 여기 . 앞에 띄우기 되도 못찰을수도 있음 
print(Line)
print(Line[:3])
print(type(Line))
All = re.findall(r'All.+', script101)
print(All)
# All 의 마지막 대사 
print(All[-1])
print(len(All))
print('===================================================================')
#  출연진만 출력
# re.compile() 패턴만 찾아서 반환
act = re.compile(r'[A-Z][a-z]+:') # 첫글자를 영어 대소 문자 a 부터 z 까지 지정하고 
# 그다음 다른 글들이 있음을 + 해주고 , 끝부분이 : 이라는 지정을 하는것 
print(re.findall(act,script101))

# 위 그대로 하면 해당하는걸 반복적으로 출력하게 되는데 
# ##################################
a = [1, 2, 3, 4, 5]
print(a)
print(set(a))
y = set(re.findall(act,script101))
print(type(y))
lst = list(y)#dict 을 list 로 형변환 
print(type(lst))
print(lst)
print(y)
# 위 그대로는 '출연진:' 으로 출력되는데 : 없어지고 출연진만 출력되게 하기 
char = []
char3 = []
# 바로 출력할수 없으니 리스트를 만들고
for i in lst : 
    # print(i[: -1])  / 이거는 : 만 제외하고 출력한다 
    char += [i[:-1]]  # 노란색 [] 를 없애면 한글 한글 넣어서 출력하게 된다 .. 그래서 [] 을 이용해서
char.sort() # char 을 정렬 해준다 
    # char3 += [i[:-1]]
    # 묵어서 출력해준다 

# 만든 이스트에 처음부터 끝까지를 넣어 준다 
print('출연진 : ', char)
# print('출연진 : ', char3)
print(len(char))


char2 = []
for i in lst : 
    ch = re.sub(':','',i)
    char2.append(ch)
char2.sort()
print(char2)
print(len(char2))

print('-----------------------------------------------------------')
print() # 암것도 안쓰면 개행 한다

# 지문만 추출하는데 처음부터 6개만 출력
# (Note: The previously unseen parts of this episode are shown in blue text.) << 이런 형식 

# \ 를 이용해서 개행문자 나 , . 을 표현해주는 기능으로 사용할수 있다 
txt1 = re.findall(r'\([A-Za-z].+[a-z|\.]\)',script101)[:6] # 끝이 소문자도, . 도 있는것
print('txt1 >>> \n' , txt1)

# \ 를 이용해서 컴파일이 오해할수있는 구문 앞에 \ 이용해서 \( 는 시작괄호 \) 끝나는 괄호를 콕찝어서 의미
txt2 = re.findall(r'\([A-Za-z].+\.\)',script101)[:6] # . 으로 끝나는 것만 표시
print('txt2 >>> \n' , txt2)
##############################################
# 메일 주소만 출력하게 만들기
a = '제 이메일 주소는 greate@naver.com'
a += ' 오늘은 today@naver.com 내일은 apple@gmail.com   life@abc.co.kr 라는 메일을 사용합니다.'
print(a) 
# 메일 주소만 출력하게 만들기 / 패턴으로 지정
a1 = re.findall(r'[a-z]+.com',a)
a2 = re.findall(r'[a-z]+@[a-z]+',a)
a3 = re.findall(r'[a-z]+@[a-z.]+',a) # 여기서 [a-z.] 에서 . 은 여러가지 문자를 의미 

print(a1)
print(a2)
print(a3)

words = ['apple', 'cat','brace','dream','asise','blow','coat','above']
# a 로 시작하는 단어 출력
alist = []
for i in words :
    alist += re.findall(r'a[a-z]+',i)
print('alist : ' , alist)

for i in words:
    blist = re.search(r'a[a-z]+',i)
    if blist:
        print(blist.group()) # blist 객체가 생성되지 않은 상태에서 group() 사용해서 오류 

print()

for i in words:
    # m = re.match(r'a[a-z]+',i) # pattern 을 문자열의 첫부분과 비교 
    m = re.match(r'a\D+',i) # d 숫자를 의미 D 은 숫자가 아닌 ! 그표현을 지정하기 위해 \ 사용
    if m: # m 이 있다면 
        print(m.group()) # 그룹으로 문자열 출력