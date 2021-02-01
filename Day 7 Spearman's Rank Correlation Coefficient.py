# Enter your code here. Read input from STDIN. Print output to STDOUT

#set input
n=int(input())
x=list(map(float,input().strip().split()))
y=list(map(float,input().strip().split()))

#code to calculate rank and d
rx = [sorted (x).index(i) for i in x]
ry = [sorted(y).index(i) for i in y]
d_sq = sum([(rx[i]-ry[i])**2 for i in range(n)])

#code to Spearman's rank correlation coefficient
rxy = 1- (6 * d_sq) / (n * (n**2 -1))
print(round(rxy,3))