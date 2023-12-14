from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id="meigen">
            <h1>위키북스 도서</h1>
            <ul class="items">
                <li>유니티 게임 이펙트 입문</li>
                <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                <li>모던 웹사이트 디자인의 정석</li>
            </ul>
        </div>
    </body></html>
"""

# 문제
# 위키북스 도서 출력 => find
# 위키북스 도서 출력 => select

soup = BeautifulSoup( html , 'html.parser')
print(soup)
h1 = soup.html.body.h1
print(h1)
print(h1.text)
h2 = soup.select_one('h1')
print(h2)
print(h2.text)
h3 = soup.find('h1')
print(h3)
print(h3.text)

# li 만 출력
print('====================')

h1 = soup.html.body
h1 = h1.ul
h1 = soup.select('div#meigen > ul.items > li').string

print(h1)
print('====================')
h3 = soup.find('li')
print(h3)
print(h3.text)

# h2 = soup.select_one('h1')
# print(h2)
# print(h2.text)
# h3 = soup.find('h1')
# print(h3)
# print(h3.text)