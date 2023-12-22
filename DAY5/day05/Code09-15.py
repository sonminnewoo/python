import bs4
import urllib.request

# 함수 선언
# ['황금종이 1', '조정래', '해냄', '2023년 11월', '16,650']
def getBookInfo(book_tag):
  names = book_tag.find('div', {'class' : 'goods_name'})
  bookName = names.find('a').text
  auths = book_tag.find('span', {'class' :'goods_auth' })
  bookAuth = auths.find('a').text
  bookPub = book_tag.find('span', {'class' :'goods_pub' }).text
  bookDate = book_tag.find('span', {'class' :'goods_date' }).text
  bookPrice =  book_tag.find('em', {'class' :'yes_b' }).text
  return [bookName,bookAuth,bookPub,bookDate,bookPrice]

## 전역 변수부
url = "http://www.yes24.com/24/Category/Display/001001046001?PageNumber="
PageNumber = 1

# bookUrl = http://www.yes24.com/24/Category/Display/001001046001?PageNumber=1

## 메인 코드부
books = []
while True:
  try:
    bookUrl = url + str(PageNumber)
    PageNumber += 1
    htmlObject = urllib.request.urlopen(bookUrl)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    # ['황금종이 1', '조정래', '해냄', '2023년 11월', '16,650']
    # ['황금종이 2', '조정래', '해냄', '2023년 11월', '16,650']
    tag = bsObject.find('ul', {'class' : 'clearfix'})
    all_books = tag.find_all('div', {'class' : 'goods_info'})

    for book in all_books:
      b = getBookInfo(book)
      books.append(b)
      print(b)

  except:
    break
#  pandas   사용하여 제목 저자 출판사 출판일 가격
# book_yes.csv  
  
import pandas as pd 
dfbooks = pd.DataFrame(books, 
          columns=('제목', '저자', '출판사', '출판일', '가격')) 
dfbooks.to_csv('book_yes.csv',encoding='utf-8-sig',index=False) 
