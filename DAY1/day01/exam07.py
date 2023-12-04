# 1에서 10까지 합계를  while
i = 1
hap = 0
# i, hap = 1, 0
while  i < 11   : 
  hap += i
  i = i+ 1

print(hap)
print ("======")

sum = 0
while True:
  sum += 1
  if sum > 5:
    break
print(sum)
print ("======")  

for i in range(1, 10):
  if i % 3==0 :
    break
  print(i)

  

