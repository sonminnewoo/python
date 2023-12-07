#  과제 

nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]
# 전역변수

def max_count(nums) :
    nums = dict()
    nums = {
        1 : 4,
        2 : 4,
        3 : 5
    }
    return set(nums.items())

counts = max_count(nums)
print(counts)   # {1:4 , 2:4 , 3:5}

# 아래 다른 버전

def max_count(nums) :
    v1,v2,v3 = 0,0,0
    for i in range(0,len(nums)) :
        if nums[i] == 1 :
            v1 += 1
        elif nums[i] == 2 :
            v2 += 1
        elif nums[i] == 3 :
            v3 += 1
    nums = {
        1 : v1,
        2 : v2,
        3 : v3
    }
    return nums
