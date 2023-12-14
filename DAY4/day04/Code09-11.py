# https://news.nate.com/ 접속해서
# 오늘  종합  최신뉴스  정치  경제  사회  세계  IT/과학  칼럼  포토  TV  라디오  랭킹뉴스  투데이댓글  
import urllib.request
import bs4

nateUrl = "https://news.nate.com/"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'class' :'snbArea' })
print('## 네이트 뉴스의 메뉴 목록00 ##')
li_list = tag.findAll('li')
for li in li_list:
  print(li.text, end= ' ')

print()
print('## 네이트 뉴스의 메뉴 목록11 ##')  
tag = bsObject.find('div', class_ = 'snbArea')
li_list = tag.find_all('li')
for li in li_list:
  print(li.text, end= ' ')

print()
print('## 네이트 뉴스의 메뉴 목록 select ##')   
# tag = bsObject.select_one('div.snbArea')
#header > div.navWrap > div
tag = bsObject.select_one('#header > div.navWrap > div')
#header > div.navWrap > div > ul > li.on > h1 > a
li_list = tag.select('li')
for li in li_list:
  print(li.string, end= ' ')





