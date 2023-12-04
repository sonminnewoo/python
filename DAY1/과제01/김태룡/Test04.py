def max_count(nums):
    num1 = nums.count(1)
    num2 = nums.count(2)
    num3 = nums.count(3)
    
    numCount = {1:num1 , 2:num2 , 3:num3}
    return numCount

if __name__ == "__main__":
    nums = [1,1,1,2,2,3,2,3,2,3,3,3,1]
    counts = max_count(nums)
    print(counts)