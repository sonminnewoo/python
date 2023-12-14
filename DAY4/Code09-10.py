import urllib.request
import bs4

nateUrl = "https://www.nate.com"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage,'html.parser' )

tag = bsObject.find('div', {'id' : 'NateBi'})
print(tag)
print('=============================')
tag_href = tag.find('a')
print(tag_href)
print(tag_href['href'])
print(tag_href.text)