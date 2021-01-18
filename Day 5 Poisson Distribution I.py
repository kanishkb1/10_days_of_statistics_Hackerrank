from math import factorial
mean=float(input())
k=int(input())
e=2.71828

result = ((mean**k) * (e**-mean)) / factorial(k)
print(round(result,3))