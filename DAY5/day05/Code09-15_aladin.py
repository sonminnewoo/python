import bs4
import requests

# 함수 선언
# 책제목, 저자 ,가격
def getBookInfo(book_tag):
  #저자
  authorName = book_tag.find('div', {'class' : 'b-author'}).text
  # 가격
  # p = book_tag.find('div', {'class' : 'b-price'})
  # price = p.find('strong').text
  price = book_tag.select_one('div.b-price > strong').text
  # 책제목
  bookName =book_tag.find('a').text
  return [bookName,authorName,price]
  

## 전역 변수부
bookUrl = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351' 
htmlObject = requests.get(bookUrl)
bsObject = bs4.BeautifulSoup(htmlObject.content, 'html.parser')

tag = bsObject.find('ul', {'class' : 'b-booklist'})
all_text = tag.findAll('div', {'class' : 'b-text'})
# 책제목, 저자 ,가격 가져오기
for book in all_text:
  print(getBookInfo(book))







