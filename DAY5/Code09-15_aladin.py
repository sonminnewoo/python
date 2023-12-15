# 알라딘도 밑에 해보기 
# https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351
# 에서 MD 추천 신간 찾아오기 
 
import bs4
import requests

#함수선언

def getBookInfo(book_tag):
    #저자
    authorName = book_tag.find('div', {'class' : 'b-author'}).text
    # #가격
    # p = book_tag.find('div', {'class' : 'b-price'})
    # price = p.find('strong').text
    # ▲ 위 처럼 해도되고 ▼아래처럼 해도 된다
    price = book_tag.select_one('div.b-price > strong').text
    

    # 지정을 받아온 인수에서 바로 지정할수 없으니 p 로 연결해서 , p로 다시 원하는걸
    # 찾아오게 된다

    #책제목
    bookName = book_tag.find('a').text

    return [bookName,authorName,price]

# 전역 변수부

url = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351'
htmlObject = requests.get(url)
bsObject = bs4.BeautifulSoup(htmlObject.content, 'html.parser' )

tag = bsObject.find('ul' , {'class' : 'b-booklist'})
all_text = tag.findAll('div', {'class':'b-text'})
# 책제목, 저자 , 가격 가져오기 >> 함수 getBookInfo 가 반환할 항목

for book in all_text :
    print(getBookInfo(book))