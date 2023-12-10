import re

exemple = '저는 (91년) 에 태어났습니다. (97년) 에는 imf 가 있었습니다. 지금은 (2023년)입니다.'

print(exemple)

# ['(91년)', '(97년)', '(2023년)']

txt = re.findall(r'\(\d+년\)',exemple)  
# r'' 사이에 \( 하면 ( 괄호 지정 , \d 하면 숫자 +년\) 하면 형태를 지정하게된다 
print(txt)
txt1 = re.findall(r'\(\d.+년\)',exemple)  
# r'' 사이에 \( 하면 ( 괄호 지정 , \d 하면 숫자 +년\) 하면 형태를 지정하게된다 
print(txt1)
txt2 = re.findall(r'\(\d.+?년\)',exemple)  
# r'' 사이에 \( 하면 ( 괄호 지정 , \d 하면 숫자 +년\) 하면 형태를 지정하게된다 
# ? 는 0~9 이하 를 의미 해서 . 을 적을경우 원하는 숫자까지만 지정하려면 ? 를 넣어준다
print(txt2)