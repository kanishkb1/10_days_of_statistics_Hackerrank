n=int(input())
x=list(map(int,input().split()))
x.sort()

def get_median(x):
    if len(x) % 2==0:
        return (x[len(x) // 2] + x[len(x) // 2 - 1]) //2
    else:
        return x[len(x)//2]
    
if len(x) % 2==0:
    q2 = get_median(x)
    q1 = get_median(x[: len(x) // 2])
    q3 = get_median(x[len(x) // 2 :])
 
else:
    q2 = x[len(x) // 2]
    q1 = get_median(x[: x.index(q2)])
    q3 = get_median(x[x.index(q2) + 1 :])

print(q1)
print(q2)
print(q3)
