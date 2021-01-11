from math import sqrt

#Step-1: set data
n=int(input())
x=list(map(int,input().split()))

#Step 2: Calculate mean
def get_mean(x):
    return sum(x) / n

#Step 3: Calculate standard deviation

deviation =sum([(x[i]-get_mean(x))**2 for i in range(n)])

#Step-4: Calculate variance
variance = sqrt(deviation/n)
print(variance)



        