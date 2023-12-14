from bs4 import BeautifulSoup
import requests

res = requests.get('http://media.daum.net/digital/')
# print(res.content)

soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)
li_list = soup.find('ul', {'class' : 'list_mainnews'})
print(li_list)

for i in li_list.find_all('a', 'link_txt'):
  print(i.text.strip())
