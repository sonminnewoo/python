from bs4 import BeautifulSoup
import requests

url = "http://finance.naver.com/marketindex/"
res  = requests.get(url)

soup = BeautifulSoup(res.content,'html.parser')
# print(soup)
#exchangeList > li.on > a.head.usd > div
txt = soup.select_one('#exchangeList > li.on > a.head.usd > div')
print(txt)
print('value  >> : ' , txt.select('span')[0].string)
print('blind  >> : ' , txt.select('span')[4].string)
print('-----')
txt2 = txt.select('span')
print(txt2)
for sp in txt2:
  print(sp.string)
print('-----')  
#exchangeList > li.on > a.head.usd > div > span.value
price = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').string
#exchangeList > li:nth-child(1) > a.head.usd > div > span.blind
updown = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.blind').string
print('price :' ,price)
print('updown :' ,updown)
print('-----') 
price = soup.select_one('div.head_info > span.value').string
#exchangeList > li:nth-child(1) > a.head.usd > div > span.blind
updown = soup.select_one('div.head_info > span.blind').string
print('price :' ,price)
print('updown :' ,updown)

# //*[@id="exchangeList"]/li[1]/a[1]/div