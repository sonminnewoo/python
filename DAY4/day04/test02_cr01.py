from bs4 import BeautifulSoup

html = """
  <html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
  </body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
print(soup)
print("-------")
h1 = soup.html.body.h1
print("h1 >> ", h1)
p = soup.html.body.p 
print("p >>> ", p)
p1 = p.next_sibling.next_sibling
print("p1 >>> ", p1)
print("-------")
h1 = soup.find('h1')
print("h1 : ", h1)
p = soup.find('p')
print("p :", p)
p_list = soup.findAll('p')
print("p_list :", p_list)
print('========select ====')
h1 = soup.select_one('h1')
print("h1 : ", h1)
p= soup.select_one('p')
print("p :", p)
p_list = soup.select('p')
print("p_list :", p_list)
print('========문자만 출력 ====')
print(h1.text)
print(p.string)
print("p_list [] : ", p_list[1].text)