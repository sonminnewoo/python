# https://movie.daum.net/ranking/reservation
# 제목 폄점 예매율 

import bs4
from bs4 import BeautifulSoup
import requests

URL = 'https://movie.daum.net/ranking/reservation'
res = requests.get(URL)
# ▲ 위 내용을 한줄로 하려면 
# res = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(res.content, 'html.parser')
txt = soup.select_one('#mainContent > div > div.box_ranking > ol')
# print(txt)

# txt = txt.find_all('div', {'class' : 'thumb_cont'})
# print(txt)
# for i in txt:
#     print(i.text)

# ▲ 내가 한거 : 문제는 중간에 공백이 너무 크게 발생한다 >> 이유 : 한개 큰단위를 읽어온걸 for 문 으로 출력하기때문에 중간의 공백이 표시되어버림
# ▼ 선생님 한거 : 내꺼의 문제를 선생님은 항목별로 찾는 방식으로 원하는 값을 구한다음 , 그값을 변수 에 넣고 원하는 방식으로 출력을 한다 

lis = txt.select('li')
# print(lis)
for i in lis:
    movieTitle = i.find('a', class_='link_txt').get_text()
    movieGrade = i.find('span', class_='txt_grade').string
    movieReser = i.find('span', {'class': 'txt_num'}).get_text()
    print('영화 : ', movieTitle, end=' / \n')
    print('평점 : ', movieGrade, end=' / \n')
    print('예매율 : ', movieReser, end=' / \n')

# find 버전 
print('-----------------------------------\n')
# select 버전

for i in lis:
    movieTitle = i.select_one('a.link_txt').get_text()
    movieGrade = i.select_one('span.txt_grade').string
    movieReser = i.select_one('span.txt_num').get_text()
    print('영화 : ', movieTitle, end=' / \n')
    print('평점 : ', movieGrade, end=' / \n')
    print('예매율 : ', movieReser, end=' / \n')

# daummovie.csv 로 저장하기

import csv
# csv 로 읽거나 저장 하려면 이렇게 csv 객체 를 가져온다 

with open('daummovie.csv', 'w',newline='',encoding='utf-8') as csvfile:
    # with open(파일명,w 이나 r {다른 옵션도 있음} , 한줄씩 저장, 저장하는 형식지정{기본 utf-8})저장방식 과 닉네임 설정 
    csv_writer = csv.writer(csvfile)
    # 닉네임화 된 저장방식대로 csv 생성
    csv_writer.writerow(['제목','평점','예매율'])
    # 만든것에 맨처음 행에 항목을 적음 
    
    # 이후 행에 쓸 데이터 적기
    for i in lis :
        movieTitle = i.select_one('a.link_txt').get_text()
        movieGrade = i.select_one('span.txt_grade').string
        movieReser = i.select_one('span.txt_num').get_text()
        # 원하는 형식으로 변수에 저장하고
        csv_writer.writerow([movieTitle, movieGrade,movieReser])
        # 원하는 형태로 쓴다
    
print('성공적으로 생성되었습니다.')

# daummovie_pandas.csv 로 저장하기
# BeautifulSoup으로 가져온 데이터를 Pandas DataFrame으로 변환하고 CSV 파일로 저장하는 코드
# 이렇게 하는 이유는 기존에 는 print 로 내보내기 때문에 각자 저장된것이 없었다 ! 
# 그래서 각각 어떤 영역에 추가하고 그걸 출력하는 형식

import pandas as pd

movie_data = []
for i in lis :
    movieTitle = i.select_one('a.link_txt').get_text()
    movieGrade = i.select_one('span.txt_grade').string
    movieReser = i.select_one('span.txt_num').get_text()
    # 원하는 형식으로 변수에 저장하고
    movie_data.append([movieTitle, movieGrade,movieReser])
    # 원하는 형태로 쓴다

df = pd.DataFrame(movie_data)
df.to_csv('daummovie_pandas.csv', index=False,encoding='utf-8-sig', header=['제목','평점','예매율'])
# utf-8 에 -sig 를 추가하면 csv 파일 로 열었을때 한글 파일이. 깨지는현상을 방지 할수 있다 

print("pandas 형식 으로 CSV 파일이 성공적으로 생성되었습니다.")