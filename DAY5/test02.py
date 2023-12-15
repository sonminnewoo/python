from bs4 import BeautifulSoup
import requests


# Requests 방식 
URL2 = 'https://finance.naver.com/marketindex/'
res2 = requests.get(URL2)

soup = BeautifulSoup(res2.content, 'html.parser')
# print(soup)
#exchangeList > li.on > a.head.usd > div
txt = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(txt)
print('value >> : ',txt.select('span')[0].string)
print('blind >> : ',txt.select('span')[1].string)
print('---------------------------')
txt2 = txt.select('span')
print(txt2)
for sp in txt2 :
    print(sp.string, end='')
print('---------------------------')
price = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string
#exchangeList > li.on > a.head.usd > div > span.blind
#exchangeList > li.on > a.head.usd > div
# //*[@id="exchangeList"]/li[1]/a[1]/div
# 동일 한대상을 각 다르게 지정 하는것 
updown = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string
print('price : ', price)
print('updown : ', updown)

# 위키 문헌에서 저자 윤동주 의 시를 출력 

#mw-content-text > div.mw-content-ltr.mw-parser-output
URL3 = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'
res3 = requests.get(URL3)
soup3 = BeautifulSoup(res3.content, 'html.parser')
txt = soup3.select_one('#mw-content-text > div.mw-content-ltr.mw-parser-output > ul:nth-child(6) > li > ul')
print(txt.text, end='')
# 여러개 한다면 
a_list = soup3.select('#mw-content-text > div.mw-content-ltr.mw-parser-output > ul:nth-child(6) > li > ul > li a')
print('---------------------------')
# print(a_list)
for a in a_list : 
    name = a.string
    print("-",name)

b_list = soup3.select('#mw-content-text > div.mw-content-ltr.mw-parser-output > ul > li a')
print('---------------------------')
for b in b_list : 
    bname = b.string
    print("+",bname)