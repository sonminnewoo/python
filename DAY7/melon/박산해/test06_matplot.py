import bs4
import requests

header = {'User-Agent' : 'Mozilla/5.0' }

# 순위 곡명 가수 앨범 ==> 출력

def getChartInfo(Chart_tag) :
  #순위
   ranking = Chart_tag.find("span",{"class" : "rank"}).text
  #곡명
   song = Chart_tag.find("div",{"class" : "ellipsis rank01"}).text
  #가수
   singer = Chart_tag.find("div",{"class" : "ellipsis rank02"})
   singer1 = singer.find("a").text
  #앨범
   album = Chart_tag.find("div",{"class" : "wrap_song_info"})
   album1 = album.find("a").text

   return [ranking,song,singer1,album1]

## 전역 변수부
melonUrl = "https://www.melon.com/chart/"
htmlObject = requests.get(melonUrl, headers=header)
bsObject = bs4.BeautifulSoup(htmlObject.content, 'html.parser')
savechart = [] 
tag = bsObject.find('div', {'class' : 'service_list_song type02 d_song_list'})
all_text = tag.findAll('tr', {'class' : 'lst50'})
#순위 곡명 가수 앨범
for chart in all_text:
      c = getChartInfo(chart)   
      savechart.append(c)
      print(c)

#pandas 사용하여 내보내기 
import pandas as pd
dfbook = pd.DataFrame(savechart, columns = ('순위','곡명','가수','앨범'))
dfbook.to_csv('melon_chart.csv', encoding='utf-8-sig', index=False)
print('pandas파일저장')


