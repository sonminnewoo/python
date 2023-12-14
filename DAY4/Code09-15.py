import urllib.request
import bs4

# https://movie.daum.net/main 에서 ' 서울의 봄 ' 예매율 출력


url = "https://movie.daum.net/main" # 다음영화
urlopen = urllib.request.urlopen(url)
urlread = urlopen.read()
urlpage = bs4.BeautifulSoup(urlread, 'html.parser')

# 예매율 가져오기

bom = urlpage.find('span',{'class' : 'txt_num'})
print(bom)