import urllib.request
import bs4

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id' : 'NateBi'})
print(tag)
print()
# href 값 추출
a_tag = tag.find("a")
print(a_tag)
print(a_tag['href'])
print(a_tag.text)
