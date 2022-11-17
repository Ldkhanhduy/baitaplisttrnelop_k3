import numpy as d
import random

a=float(input("nhap so a bat ki:"))
x = random.choices(range(-15, 15), k=15)
x = d.reshape(x,(3,5))
print(x)
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i,j]*=a
print("a*x=",x)