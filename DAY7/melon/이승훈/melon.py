import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# User-Agent 설정
header = {'User-Agent' : 'Mozilla/5.0'}

# 멜론 차트 페이지에 GET 요청 보내기
url = 'https://www.melon.com/chart/index.htm'
page = requests.get(url, headers=header)

# BeautifulSoup 객체 생성
soup = bs(page.text, 'html.parser')

# 순위, 제목, 가수, 앨범 정보를 가져오기 위한 CSS 선택자 설정
rank = soup.select('#lst50 > td:nth-child(2) > div > span.rank')
title = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
musician = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
album = soup.select('#lst50 > td:nth-child(7) > div > div > div > a')

# 순위, 제목, 가수, 앨범 정보를 리스트로 저장
list = [[r.text, t.text, m.text, a.text] for r, t, m, a in zip(rank, title, musician, album)]

# 리스트를 데이터프레임으로 변환
df = pd.DataFrame(list, columns=('순위', '제목', '가수', '앨범'))

# 데이터프레임을 CSV 파일로 저장
df.to_csv('melon.csv', encoding='utf-8-sig', index=False)

