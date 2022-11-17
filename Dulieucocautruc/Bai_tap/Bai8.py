import numpy as d
import random

x = random.choices(range(-15, 15), k=15)
x = d.reshape(x,(3,5))
print(x)
print("x23=",x[1,2])
