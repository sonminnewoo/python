nums=[1,1,1,2,2,3,2,3,2,3,3,3,1]

def max_count(x):
    d = dict()
    count1 = 0
    count2 = 0
    count3 = 0
    for i in x:
        if i==1:
            count1 +=1
        elif i==2:
            count2 +=1
        elif i==3:
            count3 +=1
    d[1]=count1
    d[2]=count2
    d[3]=count3
    return d

counts=max_count(nums)
print(counts) #{1:4, 2:4, 3:5}