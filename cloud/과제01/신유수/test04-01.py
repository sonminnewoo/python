def max_count(nums):
	counts = {}
	for i in nums:
		if i in counts: 
			counts[i] += 1
		else:
			counts[i] = 1
	return counts

nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]
counts = max_count(nums)
print(counts) #{1:4, 2:4, 3:5}