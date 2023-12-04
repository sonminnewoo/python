def max_count(nums): 
    i,j,k=0,0,0
    for n in nums:
        if(n==1):
           i+=1
        elif(n==2):
           j+=1
        elif(n==3):
           k+=1  
    counts = {1: i, 2: j, 3: k}
    return counts

nums =[1,1,1,2,2,3,2,3,2,3,3,3,1]

counts = max_count(nums)
print(counts)