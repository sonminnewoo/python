nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]

def max_count(v1) :
    count_1, count_2, count_3 = 0, 0, 0
    for num in nums :
        if num == 1 :
            count_1 += 1
        elif num == 2 :
            count_2 += 1
        elif num == 3 :
            count_3 += 1
    counts = {1: count_1, 2: count_2, 3: count_3}        
    return counts

counts = max_count(nums)
print(counts) # 출력값 {1:4, 2:4, 3:5}