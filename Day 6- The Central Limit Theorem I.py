import math
#Set input data
x=9800
n=49
mean=205
std=15

#Set function for central limit theorom
# The sum of these random variables will converge to a normal distribution (provided n is big enough) with mean 
sum_mean = n * mean
sum_std = math.sqrt(n) * std
  
def central_theorem (x,mean,std):
    z = (x - mean) / std
    return 0.5 * (1 + math.erf(z / 1.414))


#set output
answer = central_theorem(x,sum_mean,sum_std)
print(round(answer,4))