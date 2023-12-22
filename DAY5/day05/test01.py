from bs4 import BeautifulSoup
import re

html = """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa</li>
    </ul>
"""
soup = BeautifulSoup(html, 'html.parser')
a_lis = soup.find_all('a')
print(a_lis)
for i in a_lis : 
  print(i['href'])
print('-----------')
# https로 시작하는 출력
# <a href="https://example.com/fuga">fuga*</a>, 
# <a href="https://example.com/foo">foo*</a>

lis = soup.find_all(href=re.compile(r'https://'))  # https가 포함
print(lis)
print('-----------')
lis = soup.find_all(href=re.compile(r'^https://'))  # https가 시작
print(lis)
print('-----------')
lis = soup.findAll(href=re.compile(r'^https://'))  # https가 시작
print(lis)

# https://example.com/fuga  , https://example.com/foo  출력
for i in lis:
  print(i.text)
  print(i.attrs['href'])