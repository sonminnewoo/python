########################################################################
# 책 370 페이지 , yes24 에서 책정보를 가져오는데 ! 
# 페이지마다 조회 해서 정보를 가져오게 하는것 
import bs4
import urllib.request
import pandas as pd

url = 'https://www.yes24.com/24/Category/Display/001001046001?PageNumber='
# # ?PageNumber= 로 전역변수를 지정해준다 

PageNumber = 1 
# # 일종의 페이지를 부여하기 위해 지정해준다 
# # https://www.yes24.com/24/Category/Display/001001046001?PageNumber=1

#함수선언
def getBookInfo(book_tag):
    names = book_tag.find('div', {'class' : 'goods_name'})
    bookName = names.find('a').text
    auths = book_tag.find('span', {'class' : 'goods_auth'})
    bookAuth = auths.find('a').text
    bookPub = book_tag.find('span' , {'class' : 'goods_pub'}).text
    bookDate = book_tag.find('span', {'class' : 'goods_date'}).text
    bookPrice = book_tag.find('em', {'class' : 'yes_b'}).text
    return [bookName,bookAuth,bookPub,bookDate,bookPrice]

# 메인코드부
books = []
d = 0 
while(d<20):
    try :
        bookUrl = url + str(PageNumber)
        # print(bookUrl) 위아래만 있으면 yes24 에 있는 한국소설 페이지를 계속읽게되고
        # 더이상 읽을게 없어서 오류가 나면 , 에러가 발생해서 except 로 반복구문을 나온다
        PageNumber +=1
        # 계속해서 다음페이지 내용을 읽기 위함 
        htmlObject = urllib.request.urlopen(bookUrl)
        # 데이터 받고
        webPage = htmlObject.read()
        # 받은데이터 읽고
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        # 읽어온 내용을 html 의 태그 형식 으로 파싱한다
        
        tag = bsObject.find('ul', {'class' : 'clearfix'})
        all_books = tag.findAll('div', {'class':'goods_info'})

        for book in all_books :
            b = getBookInfo(book)
            books.append(b)
            print(b)
            # print(getBookInfo(book))
        d+=1

    except : # 오류가 발생하면 종료
        break

# pandas 사용해서 'book_yes.csv' 사용해서 제목 , 저자 , 출판사, 출판일 , 가격
    
df = pd.DataFrame(books,columns=('제목','저자','와우','출판일','가격'))
df.to_csv('book_yes.csv', index=False, encoding='utf-8-sig')
