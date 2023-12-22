from bs4 import BeautifulSoup
import requests

url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
#mw-content-text > div.mw-content-ltr.mw-parser-output > ul:nth-child(6) > li > ul
a_list = soup.select('#mw-content-text > div.mw-content-ltr.mw-parser-output > ul:nth-child(6) > li > ul>li a')
# print(a_list)
for a in a_list:
  name = a.string
  print("-", name)

print('-----------') 
a_list = soup.select('#mw-content-text > div.mw-content-ltr.mw-parser-output > ul >li a')
# print(a_list)
for a in a_list:
  name = a.string
  print("-", name) 