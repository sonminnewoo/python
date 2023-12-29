# 좋아요 수가 5만 이상 , 8 만 이상 , 10만 이상

from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pandas as pd
import pymysql as py


driver = wd.Chrome()
driver.implicitly_wait(2)
driver.get('https://www.melon.com/chart/index.htm')

tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
trs = tbody.find_elements(By.TAG_NAME, 'tr')

datas = []
# datadic =  {'5만': [], '8만': [], '10만': [] }
datadic =  {'5만': 0, '8만': 0, '10만': 0 }

for tr in trs:
    rank = tr.find_element(By.CLASS_NAME, 'rank').text
    title = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank01').find_element(By.TAG_NAME, 'a').text
    singer = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank02').find_element(By.TAG_NAME, 'a').text
    album = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank03').find_element(By.TAG_NAME, 'a').text
    like_text = tr.find_element(By.XPATH, './/td[8]/div/button/span[2]').text

    like = int(like_text.replace(',', ''))
    
    if(80000 > like > 50000 ):
        # datadic['5만'].append([rank, title, singer, album, like])
        datadic['5만'] += 1
    elif(100000 > like > 80000 ):
        # datadic['8만'].append([rank, title, singer, album, like])
        datadic['8만'] += 1
    elif(like > 100000 ):
        # datadic['10만'].append([rank, title, singer, album, like])
        datadic['10만'] += 1
    

print(datadic)

# 차트 만드는 라이브러리 출력
import matplotlib.pyplot as plt
import matplotlib as mpl 
font_name = mpl.font_manager.FontProperties(fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font',family =font_name)

# 데이터 프레임으로 변환
df = pd.DataFrame.from_dict(datadic, orient='index', columns=['Count'])

# PIE 차트 생성
plt.pie(df['Count'], labels=df.index, autopct='%1.1f%%', startangle=90)
plt.title('Likes Distribution')
plt.show()



# cur.execute(create_table_sql)

# driver = wd.Chrome()
# driver.implicitly_wait(2)
# driver.get('https://www.melon.com/chart/index.htm')

# tbody = driver.find_element(By.XPATH, '//*[@id="frm"]/div/table/tbody')
# trs = tbody.find_elements(By.TAG_NAME, 'tr')

# datas = []

# for tr in trs:
#     rank = tr.find_element(By.CLASS_NAME, 'rank').text
#     title = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank01').find_element(By.TAG_NAME, 'a').text
#     singer = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank02').find_element(By.TAG_NAME, 'a').text
#     album = tr.find_element(By.CSS_SELECTOR, 'div.ellipsis.rank03').find_element(By.TAG_NAME, 'a').text
#     like_text = tr.find_element(By.XPATH, './/td[8]/div/button/span[2]').text

    
#     like = int(like_text.replace(',', ''))

#     datas.append([rank, title, singer, album, like])

# print(datas)

# insert_sql = "INSERT INTO melonsq(melon_rank, title, singer, album, melon_like) VALUES (%s, %s, %s, %s, %s)"

# for data in datas:
#     cur.execute(insert_sql, data)

# con.commit()
# con.close()
