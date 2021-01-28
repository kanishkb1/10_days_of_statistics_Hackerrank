# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

#set data
mean, std = list(map(int,input()))
n1 = int(input())
n2 = int(input())

#Function for normal distribution
def normal(mean,std,x):
    return 0.5 * (1 + math.erf((x-mean) / (1.414 * std)))

#Output

print(round((1-normal(mean,std,n1))*100,2))
print(round((1-normal(mean,std,n2))*100,2))
print(round((normal(mean,std,n2))*100,2))
    
