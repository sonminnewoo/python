from bs4 import BeautifulSoup

html = """
    <html><body>
        <h1>스크린레이핑이란</h>
        <p>웹 페이지를 분석하는 것</p>
        <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""

soup = BeautifulSoup( html, 'html.parser')
print(soup)
print('==========================')
h1 = soup.html.body.h1
print(h1)
# h1 안의 값만 출력
print('************************1')
p = soup.html.body.p
# p 에 soup.html.body.p 넣고
# 첫번째 p 를 지정한것
print(p)
print('************************2')
p1 = p.next_sibling
# 첫번째 p 의 다음것을 지정하는것 , 처음 p 와 두번째 p 사이에 우리눈에는 없지만
# 컴퓨터 입장에서는 공백 으로 구분을 짓는가보다 공백만 출력된다

# 다음을 찾아 넣는것 ./ 위에서 p 에 soup.html.body.p 을 넣은것의 다음
print(p1)
print('************************3')
p2 = p.next_sibling.next_sibling
# 첫번째 p 의 다음것을 지정하는것 에 다음것을 지정한것 그래서 두번째 p 값이 출력됨
print(p2)
print('************************4')

#  추출할때 편한걸 사용하면 된다 

h1 = soup.find('h1')
p = soup.find('p')

print("h1 : ", h1 )
print("p : ", p )
p_list = soup.findAll('p')
print('p_list :',p_list)
print('======================')
h1 = soup.select_one('h1')
print(' p : ', p)
p_list = soup.select('p')
print('===========================')
print('p_list : ', p_list)
print('=======문자만 출력========')
print(h1.text)
print(p.string)
print('p_list [] : ', p_list[1].text)