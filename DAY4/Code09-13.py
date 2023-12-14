import requests
from bs4 import BeautifulSoup

# res = requests.get('https://www.dhlottery.co.kr/gameResult.do?method=byWin')
# soup = BeautifulSoup(res.content, 'html.parser')
# ballNum = soup.find_all('span', class_ = 'ball')
# print(ballNum)
# for i in ballNum:
#     # print(i.text, end='\t')
#     print(i.get_text(), end='\t')
# print('\n---------------------')
# #cibtauner > div div.bx_lotto_winnum > span.ball
# nums = soup.select('#d#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p ')
# for li in nums:
#     print(li.text)


import requests
from bs4 import BeautifulSoup
import bs4

res = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=byWin')
soup = BeautifulSoup(res.content, 'html.parser')
# ballNum = soup.find_all('span', class_ ='ball')
ballNum = soup.find_all('span', class_ ='ball')
# print(ballNum)
for i in ballNum:
#   print(i.text, end='\t') 아래 방식으로도 출력할수 있다 
#   print(i.string, end='\t') 아래 방식으로도 출력할수 있다 
  print(i.get_text(), end='\t')
print('\n------------------') 
#container > div > div.bx_lotto_winnum > span.ball 
nums = soup.select('#container > div > div.bx_lotto_winnum > span.ball')
# print(nums)
for i in nums:
#   print(i.string, end ='\t') 아래 방식도 있다
  print(i.text, end ='\t')