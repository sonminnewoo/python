import urllib.request
# 웹에 접속하기위한 객체 import
import bs4
# 읽어들인 웹의 태그로 어지럽게 되어있는걸 html 형태로 바꿔 주는것 

nateUrl = "https://www.nate.com"
# 대상을 변수에 넣고 
htmlObject = urllib.request.urlopen(nateUrl)
# url 을열고
print(htmlObject.read())
# 열었던 url 내용을 읽다
# print(html)
bsObject = bs4.BeautifulSoup(htmlObject,'html.parser')
print(bsObject)