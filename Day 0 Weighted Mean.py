n=int(input())
x=list(map(int,input().split()))
w=list(map(int,input().split()))
numerator=0.0
denominator=0
for i in range(n):
    numerator+=x[i]*w[i]
    denominator+=w[i]
mean=round(numerator/denominator,1)
print(mean)
