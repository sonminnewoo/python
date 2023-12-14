import bs4

webPage = open('./python/cloud/HTML/Sample03.html','rt',encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser') # html 만 파싱
# 문서 읽기 
tag_li_all = bsObject.findAll('li')
print(tag_li_all)
# print(tag_li_all.text)  >>> 이걸는 오류가 발생한다 리스트 형태를 값만 추출할수 없기때문
# 좀더 ! 자세히 그런 펑션을 python 이 안만듬 . 그래서 우리는 힘들게 아래처럼 해줘야 한다 

for i in tag_li_all : 
    print(i.text) # 이렇게 한개을 value 만 지정했을때는 오류 가 발생하지 않는다
print()

for i in range(len(tag_li_all)) : 
    print(tag_li_all[i].text)

