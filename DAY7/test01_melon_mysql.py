import requests
from bs4 import BeautifulSoup

header = {'User-Agent' : 'Mozilla/5.0'}
req = requests.get('https://www.aladin.co.kr/shop/wbrowse.aspx?CID=351')