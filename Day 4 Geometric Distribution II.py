#Setting data
num,den= list(map(int,input().split()))
n=int(input())
p=float(num/den)

#Calculating binomial distribution
q= 1-p
binomial = q**(n-1) * p
print(round(binomial,3))
