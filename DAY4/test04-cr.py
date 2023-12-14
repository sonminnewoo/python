# select 와 find 사용해서 웹페이지 데이터 가져오기 

#  import urllib.request
# import bs4

# nateUrl = "https://news.daum.net/digital#1"
# htmlObject = urllib.request.urlopen(nateUrl)
# webPage = htmlObject.read()
# bsObject = bs4.BeautifulSoup(webPage,'html.parser' )

# tag = bsObject.find('ul',{'class':'list_mainnews'})
# # print(tag)

# tag_list = tag.findAll('strong')
# for li in tag_list : 
#     print(li.text)

########################################################
from bs4 import BeautifulSoup
import requests

# URL = 'https://news.daum.net/economic#1'
# res = requests.get(URL)
# # 위의 리드와 같다 , 좀더 간단해진다 
# res.content

# soup = BeautifulSoup(res.content, 'html.parser')
# # print(soup)

# li_list = soup.find('ul',{'class':'list_mainnews'})
# # print(li_list)

# for i in li_list.find_all('a','link_txt') : 
#     print(i.text.strip())

##########################################################
import re
URL2 = 'https://news.daum.net/economic#1'
res2 = requests.get(URL2)
res2.content

soup = BeautifulSoup(res2.content, 'html.parser')
# li_list2 = soup.find('ul',{'class' : 'list_mainnews'})
# for i in li_list2.find_all('a','link_txt') :
#     print(i.text)

# re 에서  . : 임의의 문자
# \w 숫자와 문자
links = soup.select('a[href]')
print('len link >>', len(links))


result = []
for i in links :
    if re.search(r'https://v.\w', i['href']) :
        print(i.text.strip())
        result.append(i.text.strip())

print(result)
print('len result >>', len(result))
