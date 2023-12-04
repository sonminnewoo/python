import requests # 을 이용해서 네이버엔

URL = 'http://www.naver.com'
response = requests.get(URL)
print(response) # 결과 값이 200 이 나오면 성공이라고 한다 
print(response.text) # 이렇게 하면 소스들이 커멘드 창으로 출력이 된다 .