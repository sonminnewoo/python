import bs4

webPage = open('./python/cloud/HTML/Sample01.html','rt',encoding='utf-8').read()
# print(webPage)
# 위처럼도 읽을수 있고 
print('================')

# import bs4 객체를 추가해서 그 기능으로 출력할수 있다
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
print(bsObject)

# find 이용해서 div 라는것을 추출한다 
tag_div = bsObject.find('div')
print(tag_div)
print(tag_div.text)
print(tag_div.string)
