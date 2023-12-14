# 오늘 종합 최신뉴스 정치 경제 사회 세계 it/과학 칼럼 포토 tv 라디오
#  랭키뉴스 최신 투데이 댓글 

import urllib.request
import bs4

nateUrl = "https://news.nate.com/"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage,'html.parser' )

tag = bsObject.find('div', {'class' : 'snbArea'})
print(tag)
print('=============================')
print('## 네이트 뉴스의 메뉴 목록 00 ##')
tag_href_list2 = tag.findAll('li')
# tag_href_list2 = tag.find_all('li') 이렇게도 지정할수있다
# print(tag_href.text)
# print(tag_href['href'])

for i in tag_href_list2 : 
    print(i.text, end= ' ')

print('=============================')

tag_href_list = tag.findAll('a')
for i in tag_href_list : 
    print(i.text)

print()
print('## 네이트 뉴스의 메뉴 목록 select ##')
#header > div.navWrap > div
tag = bsObject.select_one('#header > div.navWrap > div') 
# 하나만 찾아옴 , select_one : 주석의 의미가 아닌 아이디의 의미
# print(tag)

tag_href_list2 = tag.select('li > a')
for li in tag_href_list2:
    # print(li.text, end= ' ')
    print(li.string, end= ' ') # 윗줄과 동일하다 / text,string

# 다른 방식으로 li 구현
