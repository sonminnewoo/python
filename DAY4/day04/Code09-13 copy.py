import requests
import datetime
import time
from bs4 import BeautifulSoup

nateUrl = "https://news.nate.com/weather?areaCode=11D20401"  # 속초
weather_list = ['연월일', '시분초', '온도', '습도', '강수량', '풍향']
while True:
  htmlObject = requests.get(nateUrl)
  bsObject = BeautifulSoup(htmlObject.content, 'html.parser')
  tag = bsObject.select_one('div.right_today')
  # 온도 temper
  temper =tag.select_one('p.celsius').text
  # 습도 humi
  humi = tag.select_one('p.humidity').text
  # 강수량 rain
  rain = tag.select_one('p.rainfall').text
  # 풍향 wind
  wind = tag.select_one('p.wind').text

  now = datetime.datetime.now()
  yymmdd = now.strftime('%Y-%m-%d')
  hhmmss = now.strftime('%H-%M-%S')
  weather_list.append([yymmdd, hhmmss,temper,humi,rain,wind ])
  print(weather_list)

  time.sleep(10)  










