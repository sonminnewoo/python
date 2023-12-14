from bs4 import BeautifulSoup
import requests
import re

res = requests.get('https://news.daum.net/economic/')

soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)
links = soup.select('a[href]')
print("len links >>", len(links))
# re 에서 . : 임의의 문자 
# \w 숫자와 문자
result = []
for i in links:
  if re.search(r'https://v.\w', i['href']): 
    result.append(i.text.strip()) 
 
print(result)
print("len result >> " ,len(result)) 
