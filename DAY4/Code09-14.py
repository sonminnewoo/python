
# web 접속 해서 매일 접속해서 
# 날씨정보를 읽어 온다 
# 연월일, 시분초,온도,습도,강수량,품향

import urllib.request
# url 사용
import datetime 
# 날짜 데이터 사용
import time
# 시간 데이터 사용
import bs4
# html 데이터 를 가져오게 해주는것 
# 그중 BeautifulSoup 을 사용하면 html 의 테그정보를 가져온다 
import csv
# csv 사용



csvName = './python/cloud/CSV/Code0913_weather.csv'
with open(csvName, 'w', newline='') as csvFp : 
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일','시분초','온도','습도','강수량','풍향','\n'])
    
nateUrl = "https://news.nate.com/weather?areaCode=11D20401" # 속초
 
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag = bsObject.find('div' , {'class' : 'right_today'})
temperature = tag.find('p' , {'class' : 'celsius'}).text
# print(temperature)
humi = tag.find('p' , {'class' : 'humidity'})
humi = humi.select_one('em').text
# print(humi)
rain = tag.find('p' , {'class' : 'rainfall'}).text
# print(rain.text)
wind = tag.select_one('p.wind').text
# print(wind.text)

now = datetime.datetime.now()
yymmdd = now.strftime('%Y-%m-%d')
hhmmss = now.strftime('%I-%M-%S')
# # %y : 두 자리 수의 연도 ex) 19, 20, 21

# # %Y : 네 자리 수의 연도 ex) 2019, 2020, 2021

# # %m : 0을 채운 두 자리 수의 월 ex) 01, 02 ...  11 ,12

# # %d : 0을 채운 두 자리 수의 일 ex) 01, 02 ...  30, 31

# # %I : 0을 채운 12시간제의 시간 ex) 01, 02 … 12

# # %H : 0을 채운 24시간제의 시간 ex) 00, 01 … 23

# # %M : 0을 채운 두 자리 수의 분 ex) 00, 01 ... 58, 59

# # %S : 0을 채운 두 자리 수의 초 ex) 00, 01 ... 58, 59
now_weather_list = ['연월일', '시분초', '온도', '습도', '강수량', '풍향']
for i in now_weather_list : 
    print(i)
    # .append([yymmdd, hhmmss, temperature, humi, rain, wind])
print(now_weather_list)