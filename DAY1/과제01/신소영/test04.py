# nums = [1,1,1,2,2,3,2,3,2,3,3,3,1]


# counts = max_count(nums)
# print(counts) #{1:4, 2:4, 3:5}

# #맥스카운트를 만들어서 결과가 이렇게 나오도록 해라 

def max_count(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]
result = max_count(nums)
print(result)  # {1: 4, 2: 4, 3: 5}