# 알라딘도 밑에 해보기 
# https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351
# 에서 MD 추천 신간 찾아오기 
 
import bs4
import requests
import pandas as pd

#함수선언

def getBookInfo(book_tag):
    #저자
    authorName = book_tag.find('div', {'class' : 'b-author'})
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


url = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351'
htmlObject = requests.get(url)
bsObject = bs4.BeautifulSoup(htmlObject.content, 'html.parser' )
tag = bsObject.find('ul' , {'class' : 'b-booklist'})
all_text = tag.findAll('div', {'class':'b-text'})
# 책제목, 저자 , 가격 가져오기 >> 함수 getBookInfo 가 반환할 항목

# 읽어 들인걸 파일로 출력 해보기 
Books = []
for book in all_text :
    Books.append(getBookInfo(book))
print(Books)
# 파일로 내보내기 
    
df = pd.DataFrame(Books)
df.to_csv('book_aladin.csv', index=False, encoding='utf-8-sig')

