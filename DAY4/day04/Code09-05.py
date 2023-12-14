import bs4

webPage =open('../HTML/Sample02.html','r',encoding='utf-8').read()
bsObject =bs4.BeautifulSoup(webPage, 'html.parser')

#  Sample02.html ul  만 추출
tag_ul = bsObject.find('ul')
print(tag_ul)
print(tag_ul.text)
print('---')
#  Sample02.html li  만 추출
tag_li = bsObject.find('li')
print(tag_li)
tag_li_all = bsObject.findAll('li')
print(tag_li_all)
print(type(tag_li_all))