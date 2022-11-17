import random

x=random.choices(range(-15,15),k=10)
print("x=",x)
y=random.choices(range(-15,15),k=10)
print("y=",y)
tich=0
for i in range(len(x)):
    bien=x[i]*y[i]
    tich+=bien
print("tich vo huong cua x va y la:",tich)
