# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

#set input
x=250
n=100
mean=2.4
std=float(2)

#set function for central theorem
sum_mean = n * mean
sum_std = math.sqrt(n) * std

def central_theorem(x,mean,std):
    z = (x - mean) / std
    return 0.5 * (1 + math.erf(z / 1.414))

#set output
result = central_theorem(x,sum_mean,sum_std)
print(round(result,4))
