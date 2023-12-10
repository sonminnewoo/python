nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]

def max_count(n):
    x, y, z, i = 0, 0, 0, 0
    for i in range(0, len(nums)):
       a = nums[i]
       if a==1:
           x+=1
       elif a==2:
           y+=1
       elif a==3:
           z+=1
    d = {
        '1' : x,
        '2' : y,
        '3' : z
    }
    return d

counts = max_count(nums)
print(counts) # 반환값 : {1: 4, 2: 4, 3:5}