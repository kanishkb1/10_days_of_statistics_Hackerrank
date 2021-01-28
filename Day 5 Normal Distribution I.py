import math

#set data
mean,std =list(map(int,input()))
x=input()
y1,y2=list(map(int,input()))

#Defining function for 
def normal(mean,std,x):
    return 0.5 * (1 + math.erf((x - mean) / (1.414 * std)))

#Answer of question-1
print(round(normal(mean,std,x),3))

#Answer of question-2

print(round(normal(mean,std,y2)-normal(mean,std,y1)),3)
