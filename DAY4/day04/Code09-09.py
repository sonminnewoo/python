import bs4
webPage =open('../HTML/Sample02.html','rt',encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
# tag_li_all = bsObject.findAll('li')
tag_li_all = bsObject.find_all('li')
print(tag_li_all)
# print(tag_li_all.text)  ===> 오류발생
for i in tag_li_all:
  print(i.text)
print()
for i in range(len(tag_li_all)):  # i==> 위치값 0 1 2
  print(tag_li_all[i].text)  