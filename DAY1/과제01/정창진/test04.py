nums = [1, 1, 1, 2, 2, 3, 2, 3, 2, 3, 3, 3, 1]
def max_count(ns):
    d= dict()
    d = {
        '1' : nums.count(1),
        '2' : nums.count(2),
        '3' : nums.count(3)
    }
    return d.items()


counts = max_count(nums)
print(counts)   # {1: 4, 2: 4, 3: 5}