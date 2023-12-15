# ps.

# 참여자 전부 다 까먹음 파이썬 , 자바 , HTML , JS , 데이터베이스 일부 기어글 하는정도 . 
# 좀 하는거 같은 애는 단지 GPT 활용 할뿐 , 물론 현업에서도 이게 할거지만 지금상황에서 인간을평가할때 돌일함 

##################################################################
# 복습 

# 사용 객체 추가
from bs4 import BeautifulSoup
import re
import requests
import urllib.request
import bs4

# 제시 활용되는 구문 

html = """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa</li>
    </ul>
"""

# <li><a href="https://example.com/fuga">fuga*</li>
# <li><a href="https://example.com/foo">foo*</li>
#   ▲ https로 시작하는 것 출력하기

soup = BeautifulSoup(html, 'html.parser')

a_lis = soup.find_all('a')
print(a_lis)
print(type(a_lis))
print('---------------------------')
 # re 객체를 import 후 re.compile(r'형식') 으로 https:// 을 찾는것 ^ 를 앞에 붙이면 그것으로 시작하는걸 찾는다  
b_lis = soup.find_all(href=re.compile(r'https://'))
print(b_lis)

print('---------------------------')

c_lis = soup.find_all(href=re.compile(r'^https://'))
print(c_lis)

print('---------------------------')
for i in c_lis : 
    print(i.text)
    print(i.attrs['href'])

# GPT 출력
https_links = soup.find_all('a', href=lambda href: href and href.startswith('https'))
for link in https_links:
    print(link['href'])

#  https://finance.naver.com/marketindex/ 에서 
#  ▼ 환율 과 상승 항목 출력하기 ▼

URL = 'https://finance.naver.com/marketindex/'
res = urllib.request.urlopen(URL)
webPage = res.read()
webObject = BeautifulSoup(webPage, 'html.parser')



# Requests 방식 
URL2 = 'https://finance.naver.com/marketindex/'
res2 = requests.get(URL2)

soup = BeautifulSoup(res2.content, 'html.parser')
# print(soup)
#exchangeList > li:on > a.head.usd > div
txt = soup.select_one('#exchangeList > li:on > a.head.usd > div')
print(txt)
print('value >> : ',txt.select('span')[0].string)
print('blind >> : ',txt.select('span')[1].string)
print('---------------------------')
txt2 = txt.select('span')
print(txt2)
for sp in txt2 :
    print(sp.string)
print('---------------------------')
price = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string
#exchangeList > li.on > a.head.usd > div > span.blind
updown = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string
print('price : ', price)



tag = webObject.find('div' , {'class' : 'head_info point_up'})
print(tag.text, end='')
# tag = tag.find_all()
