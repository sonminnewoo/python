import time
import bs4
import urllib.request

# 크롤링 은 원 소스로 가져오는 거이기 때문에 , 원소스를 변경하면 , 업데이트로 오류를 해결해줘야 한다
# 오류가 발생하면 담당자에게 메세지를 전달할수 있을것
# 정적 크롤링은 소스코드 로 이용한다 고 했다 

# 셀레니움이라고 하는 가상의 웹페이지에서 동적 클로링을 하는 2개 가 있다
# 1. 셀레니움 문법으로할수도 있고 , 2. 가상의 브라우저를 띄워서 소스코드를 읽게 한다 
#  분명히 표시되거나 기능하는데 , 소스코드 에 안나오면 , 동적코드 로 만들어 졌다고 알수 있다 

nateUrl = "https://news.nate.com/recent?mid=n0100"
while True : 
    htmlObject = urllib.request.urlopen(nateUrl)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag_list = bsObject.findAll('div', {'class' : 'mlt01'})

    print('#########실시간 뉴스 속보 ##########')
    num = 1
    for tag in tag_list:
        
        subject = tag.find('h2' , {'class' : 'tit'}).text
        link = tag.find('a',{'class' : 'lt1'})['href']
        pressAndDate = tag.find('span' , {'class':'medium'}).text
        pressAndDate.replace('\t','')
        pressAndDate.replace('\n','')
        
        if len(pressAndDate.split()) == 3 :
            press, pDate, pTime = pressAndDate.split()
        elif len(pressAndDate.split()) == 4 :
            press1,press2,pDate,pTime = pressAndDate.split()
            press = press1+press2
        else :
            continue

        print('(',num, ')',subject)
        print('\t https:'+link,press,pDate,pTime)
        num +=1
    
    time.sleep(120)