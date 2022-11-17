import random

x=random.choices(range(-15,15),k=10)
print("x=",x)
y=random.choices(range(-15,15),k=10)
print("y=",y)
z=[]
for i in range(len(x)):
    bien=x[i]*y[i]
    z.append(bien)
print("x*y=",z)
