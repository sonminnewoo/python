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

#  위키북스 도서 출력  ==> find
#  위키북스 도서 출력  ==> select
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.find('h1').string
print(h1)
h1_1 = soup.select_one('h1').string
print(h1_1)
h1_2 = soup.select_one('div#meigen > h1').string
print(h1_2)
# li 출력
li_list = soup.select('div#meigen > ul.items > li')
print(li_list)
for li in li_list : 
  print(li.string)

li_list  = soup.select('li')  
for li in li_list : 
  print(li.text)