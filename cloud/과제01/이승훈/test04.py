nums = [1, 1, 1, 2, 2, 3, 2 ,3, 2, 3, 3, 3, 1]

def max_count(nums):
    return {num: nums.count(num) for num in [1, 2, 3]}

counts = max_count(nums)

print(counts)