#  Sample03.html 에서  div 추출
import bs4
webPage =open('../HTML/Sample03.html','rt',encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag = bsObject.find('div')
print(tag)
tags = bsObject.findAll('div')
print(tags)
tag_li = bsObject.find('div',{'class' : 'myClass1'})
print(tag_li.text)
tag_li_all = bsObject.findAll('div', {'class' : 'myClass1'})
print(tag_li_all)
tag_li_id = bsObject.find('div',{'id' : 'myId1'})
print(tag_li_id.text)

# class myClass3 추출
li_myClass3 = bsObject.findAll('li', {'class':'myClass3'})
print(li_myClass3)

a_list = bsObject.findAll('a')
print(a_list)
print('------')
for i in a_list:
  print(i['href'])
