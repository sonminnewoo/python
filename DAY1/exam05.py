# 101 페이지
numbers = []
for num in range(0,10) : 
    # range(0,10) 반복을 하는데 0 에서 10 까지 를 지정하는 
    print(num,end=' ')
    # end 를 쓰면 옆으로 출력 한다
    numbers.append(num)
    # numbers.append(num) numbers 배열에 num 을 append (추가) 한다

print(numbers)
print(len(numbers))
# len 을 사용하면 길이가 나온다 
