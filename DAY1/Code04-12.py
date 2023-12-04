#  165 페이지
def multi(v1, v2) : # v1=100, v2=200
    retList = [] # 반환할 리스트
    retList.append(v1+v2) # 리스트에 값을 입력하는 함수 append 
    retList.append(v1-v2) # 를 이용해서 값을 받아온다 , 지정은 v1,v2 로
    return retList 

myList = multi(100,200)
print(myList)
print(myList[0])
print(myList[1])
hap = myList[0]
sub = myList[1]
print("multi()에서 도려준 값 ==> %d , %d "% (hap,sub))