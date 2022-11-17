import numpy as d
import random

x = random.choices(range(-15, 15), k=15)
y = random.choices(range(-15, 15), k=15)
x = d.reshape(x,(3,5))
y = d.reshape(y,(3,5))
print("x=",x)
print("y=",y)
#Don gian hon
print("Cach don gian")
print("x+y=",x+y)
#Cach dung vong for
print("Cach dung vong for")
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i,j]+=y[i,j]
#Thay thong cam em nhat tao mot list nua de gan cac gia tri vao nen em thay doi gia tri cua list x luon
print("x+y=",x)

