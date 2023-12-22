import urllib.request
import datetime
import time
import bs4
import csv

csvName = "../CSV/Code0913_weather.csv"
with open(csvName, 'w', newline='') as csvFp:
  csvWriter = csv.writer(csvFp)
  csvWriter.writerow(['연월일', '시분초', '온도', '습도', '강수량', '풍향'])

nateUrl = "https://news.nate.com/weather?areaCode=11D20401"  # 속초

while True:
  htmlObject = urllib.request.urlopen(nateUrl)
  webPage = htmlObject.read()
  bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
  tag = bsObject.find('div', {'class' : 'right_today'})
  # print(tag)
  # 온도 temper
  temper =tag.find('p', {'class' : 'celsius'}).text
  # 습도 humi
  humi = tag.find('p', {'class' : 'humidity'}).text
  # 강수량 rain
  rain = tag.find('p', {'class' : 'rainfall'}).text
  # 풍향 wind
  wind = tag.find('p', {'class':'wind'}).text

  now = datetime.datetime.now()
  yymmdd = now.strftime('%Y-%m-%d')
  hhmmss = now.strftime('%H-%M-%S')
  weather_list = [yymmdd, hhmmss,temper,humi,rain,wind ]
  with open(csvName, 'a', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(weather_list)
    print(weather_list)

  time.sleep(3600)  # 1시간










