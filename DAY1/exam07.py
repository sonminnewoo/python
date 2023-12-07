# 110 페이지
# 1 에서 10까지 합계를 while

i = 1
hap = 0

# i, hap = 1, 0

while i < 11 :
    hap += i
    i = i + 1

print(hap)
# ------------------------------------------------------------
# 112페이지 
sum = 0
while True : # 이것만 사용하면 무한 루프 이지만 
    sum += 1 # 증감식 
    hap = sum
    if sum > 5 : # 조건을 적고 break 해서 조건달성시 빠져 나오게 한다
        break
print(sum)

# break 은 아예 반복문을 종료 

for wow in range(1,10) : 
    if wow % 3 == 0 : # 3의 배수이면
        continue 
    print(wow)

# continue 는 다시 반복문으로 이동