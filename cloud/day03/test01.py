# import re
# example = '저는 (91년)에 태어났습니다. (97년)에는 IMF가 있었습니다. 지금은 (2023년)입니다.'
# result = re.search(r'\((.*?)\)', example)
# if result:
#     content_inside_parentheses = result.example
# print(example)
# #괄호안에 것만 출력원함
# #  출력결과는 ['(91년)','(97년)','(2023년)']
# import re

# text = "이 문자열에서 (괄호 안의 내용)을 추출하고 싶습니다."

# result = re.search(r'\((.*?)\)', text)
# if result:
#     content_inside_parentheses = result.group(1)
#     print(content_inside_parentheses)


txt = re.findall(r'\(\d+년  \)', example)
print(txt)


