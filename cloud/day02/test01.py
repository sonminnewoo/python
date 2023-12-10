nums = []
def infunc() : 
    print('양수를 입력하세요 종료는 -1')

while True:
    su = int(input())
    if su ==-1:
        break
        nums.append(su)

def max_count(nums) :
    counts = {}
    for num in nums:
        if num in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts