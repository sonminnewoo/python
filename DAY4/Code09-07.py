import bs4

webPage = open('./python/cloud/HTML/Sample03.html','rt',encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser') # html 만 파싱
# 문서 읽기 

tag = bsObject.find('div')
print(tag)
tags = bsObject.findAll('div')
print(tags)
# findAll 하면 리스트로 만들어 준다
tag_li = bsObject.find('div',{'class' : 'myClass1'})
print(tag_li.text)
tag_li_all = bsObject.findAll('div', {'class' : 'myClass1'})
print(tag_li_all)
tag_li_id = bsObject.find('div',{'id' : 'myId1'})
print(tag_li_id.text)

# class myClass3 추출

tag_li_all2 = bsObject.findAll('li', {'class' : 'myClass3'})
print(tag_li_all2)
# .text 는 findAll 을 사용한경우 !! 여러개를 지정하면 오류가 발생 한다 .

# a 태그만 출력
a_list = bsObject.findAll('a')
print(a_list)
# print(a_list.text) 대상이 여러개 여서 이렇게 하면 출력할수 없다 
# 그래서 아래 처럼 나타 내야한다 
# 이때 손민우 너가 왜! 그래야하는데 ? 라고 한다면 function 을 만들거나 , python 담당자와 전세계 python 
# 을 수용 하는 무수한 군자들의 노리를 이겨내라
for i in a_list : 
    print(i['href']) # 출력한때 속성dms ['href'] 로 지정해준다