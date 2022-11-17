import random

#Cach 1:
i=random.choices(range(-10,11),k=30)
print(i)

#Cach 2:
x=[]
while len(x)<30:
    i=random.randint(-10,10)
    x.append(i)
print(x)