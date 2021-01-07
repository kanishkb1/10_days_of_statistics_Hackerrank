def get_mean(list):
	sum=0
    for i in list:
        sum+=i
     mean=float(sum)/len(list)
     return mean   
    
def get_median(list):
    median=0.0
    size=len(list)
    list1=list
    list1.sort()
    if (size % 2 ==0):
        median=float(list1[size//2 - 1] + list1[size//2]) / 2
    else:
        median= float(list1[(size-1)/2])
    return median
    

def get_mode(list):
    mode=0
    count=0
    max=0
    list1=list
    list1.sort()
    present=0
    for i in list1:
        if (i==present):
            count+=1
        else:
            count=1
            present=i
        if (count>max):
            max=count
            mode=i
    
    return mode


n=int(input())
numbers=list(map(int, input().split()))           
print(get_mean(numbers))
print(get_median(numbers))
print(get_mode(numbers))

