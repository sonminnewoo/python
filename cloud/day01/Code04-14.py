def multi(v1, v2):  # v1 =100, v2 =200
  retList = []  # 반환할 리스트
  retList.append(v1+v2)
  retList.append(v1-v2)
  return retList

myList = multi(100, 200)
print(myList)
print(myList[0])
print(myList[1])
hap = myList[0]
sub = myList[1]
print("multi()에서 돌려준 값 ==> %d, %d" % (hap, sub))