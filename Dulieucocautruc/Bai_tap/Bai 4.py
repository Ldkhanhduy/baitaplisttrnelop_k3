import random

a=float(input("Nhap mot so bat ki tu ban phim:"))
x=random.choices(range(-10,10),k=10)
print("X=",x)
for i in range(len(x)):
    x[i]=a*x[i]
print(a,"*x=",x)