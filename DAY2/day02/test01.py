nums = []

def max_count(nums):
  counts = {}
  for i in nums:
    if i in counts:  
      counts[i] += 1
    else :   
      counts[i] = 1  
  return counts   

# 양수를 입력받아 마지막은  -1(종료) dict 형태로 출력 
print('양수를 입력하세요 종료는 -1')
while True:
  su = int(input())
  if su == -1:
    break
  nums.append(su)
# print(nums)

counts = max_count(nums)
print(counts)


