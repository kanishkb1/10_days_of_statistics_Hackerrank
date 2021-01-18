lambdas = list(map(float, input().split()))
x= lambdas[0]
y = lambdas[1]
#DAILY COST-> dc_a

dc_a = 160 + 40 * (float(x)**2 + float(x))
dc_b = 128 + 40 * (float(y)**2 + float(y))
print(round(dc_a,3))
print(round(dc_b,3))