# Enter your code here. Read input from STDIN. Print output to STDOUT
#set input
samples=100
mean=500
sd= 80
interval=0.95
z=1.95

net_sd = sd / (samples ** 0.5)

print(round(mean - net_sd*z,2))
print(round(mean + net_sd*z,2))

