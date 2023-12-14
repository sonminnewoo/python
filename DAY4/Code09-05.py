import bs4

webPage = open('./python/cloud/HTML/Sample02.html','r',encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
# 문서 읽기 


# Sample01.html ul 만 추출 

tag_ul = bsObject.find('ul')

print(tag_ul)
print(tag_ul.text)

print("==================")


# Sample01.html li 만 추출  

tag_li = bsObject.find('li')
print(tag_li)
print(tag_li.text)
print("==================")

tag_li_All = bsObject.findAll('li')
print(tag_li_All)
# print(tag_li_All.text)
print(type(tag_li.text))