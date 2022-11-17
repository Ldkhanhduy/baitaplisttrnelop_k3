import random

min = -5.7
max = 6.9
x=[]
while len(x) < 30:
    i = min + (max-min)*random.random()
    i=round(i,2)
    x.append(i)
print(x)