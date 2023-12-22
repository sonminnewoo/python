from bs4 import BeautifulSoup
import requests

# 제목 평점 예매율
req = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(req.content, 'html.parser')
#mainContent > div > div.box_ranking > ol
ols = soup.select_one('#mainContent > div > div.box_ranking > ol')
lis = ols.select('li')
# print(lis)
movie = []
for i in lis:
  movietitle = i.find('a', class_='link_txt').get_text()
  moviegrade = i.find('span','txt_grade').string
  movieReser = i.find('span', {'class' : 'txt_num'}).get_text()
  movie.append([movietitle,movietitle,movieReser])
  print('영화 : ' , movietitle, end = '/  ')
  print('평점 : ' , moviegrade, end = '/  ')
  print('예매률 : ' , movieReser)

print('----')  

for i in lis:
  movietitle = i.select_one('a.link_txt').get_text()
  moviegrade = i.select_one('span.txt_grade').string
  movieReser = i.select_one('span.txt_num').get_text()
  print('영화 : ' , movietitle, end = '/  ')
  print('평점 : ' , moviegrade, end = '/  ')
  print('예매률 : ' , movieReser)

# daummovie.csv   
with open('daummovie.csv', 'w') as file:
  print('파일저장')
  file.write('영화, 평점, 예매률\n')
  for item in movie:
    row = ','.join(item)
    file.write(row+'\n')


# daummovie_pandas.csv  
import pandas as pd 
dfMovie = pd.DataFrame(movie)
dfMovie.to_csv('daummovie_pandas.csv', encoding='utf-8-sig', 
               index=False, header=['영화','평점','예매률'])

