import re
example = '저는 (91년)에 태어났습니다. (97년)에는 IMF가 있었습니다. 지금은 (2023년)입니다.'

print(example)  

txt = re.findall(r'\(\d+년\)', example)
print(txt) #  ['(91년)', '(97년)', '(2023년)']
txt1 = re.findall(r'\(\d.+년\)', example)
print(txt1) #['(91년)에 태어났습니다. (97년)에는 IMF가 있었습니다. 지금은 (2023년)']
txt2 = re.findall(r'\(\d.+?년\)', example)
print(txt2)  #  ['(91년)', '(97년)', '(2023년)']
