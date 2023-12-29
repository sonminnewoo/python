# ['KODEX 200선물인버스2X', '2,195'], ['KODEX 코스닥150선물인버스', '3,550']
import requests
from bs4 import BeautifulSoup

codes = ['252670',  '251340']

# url ='https://finance.naver.com/item/main.naver?code=252670'
prices = []
x=[]
y=[]
for code in codes:
  url ='https://finance.naver.com/item/main.naver?code='+code
  resp = requests.get(url)
  soup = BeautifulSoup(resp.content, 'html.parser')
  #middle > div.h_company > div.wrap_company > h2 > a
  name = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string
  x.append(name)
  today = soup.select_one('div > p.no_today')
  price = today.select_one('span.blind').get_text()
  y.append(price)
  prices.append([name, price])

print(prices)  

import matplotlib.pyplot as plt
import matplotlib as mpl 
# 한글 
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font',family =font_name)

 
figure = plt.figure()
axes = figure.add_subplot(111)
# plt.ylim([1000,4000])
axes.bar(x,y)
plt.show()
