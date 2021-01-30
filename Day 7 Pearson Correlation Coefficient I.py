# Enter your code here. Read input from STDIN. Print output to STDOUT\]
#set input
n=int(input())
x=list(map(float,input().strip().split()))
y=list(map(float,input().strip().split()))

#code for pearson correlation coefficient

#mean (x & y)
mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

#standard deviation (x & y)
std_x = (sum([(i - mean_x)**2 for i in x]) / n) ** 0.5
std_y = (sum([(i - mean_y)**2 for i in y]) / n) ** 0.5

#covariance
covariance = sum([(x[i] - mean_x) * (y[i] -  mean_y) for i in range(n)])

#pearson correlation
rho = covariance / (n * std_x * std_y)

print(round(rho,3))