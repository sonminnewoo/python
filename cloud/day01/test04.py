nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]

def max_count(nums):
  counts = {}
  for i in nums:
    if i in counts:  # nums  값이 dict counts에 있음
      counts[i] += 1
    else :   # nums  값이 dict counts에 없음
      counts[i] = 1  # 맨 처음일 경우 i = 1, value = 1  counts ={1:1}
  return counts    
counts = max_count(nums)
print(counts)  # {1: 4, 2: 4, 3: 5}

# dict에서 최대 value 출력
print(max(counts.values()))
# 1 : 4 번
# 2 : 4 번
# 3 : 5 번
for k, v  in counts.items() : 
  print(k , ":", v , "번")
