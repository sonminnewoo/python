nums = []
def infunc():
    print('양수를 입력하세요 종료는 -1')
    while True : 
        su= int(input())
        if su == -1:
            break
        nums.append(su)

def max_count(nums) :
    counts = {} # dict 형태로 선언 해줌 
    for i in nums: 
        if i in counts : # nums 값이 dict counts에 있음
            counts[i] += 1
        else : # nums 값이 dict counts 에 없음 
            counts[i] = 1 # 맨 처음일 경우 i = 1 , value =1 couts ={1:1}
    return counts

infunc()
counts = max_count(nums)
print(counts)