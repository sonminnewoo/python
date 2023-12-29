import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from matplotlib import rc

rc('font', family='Malgun Gothic')

def get_info(codeNum):
    url = f'https://finance.naver.com/item/main.naver?code={codeNum}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
        
    name = soup.select_one('.wrap_company h2 a').text.strip()
    price = int(soup.select_one('.no_today .blind').text.strip().replace(',', ''))

    return {'name': name, 'price': price}

result_list = []

code_list = ['252670', '251340'] 

for code in code_list:
    result_list.append(get_info(code))

plt.figure()

names = [item['name'] for item in result_list]
prices = [item['price'] for item in result_list]

plt.bar(names, prices, color=['gray', 'black'])
plt.xlabel('종목')
plt.ylabel('가격')
plt.title('종목별 가격')

plt.show()
