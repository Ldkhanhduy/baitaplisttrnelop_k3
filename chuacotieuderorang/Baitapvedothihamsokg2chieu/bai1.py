import matplotlib.pyplot as d
import numpy as np

def PTB1(a,b,x):
    f1=a*x+b
    return f1
def PTB2(a,b,c,x):
    f2=a*x**2+b*x+c
    return f2
def PTB3(a,b,c,d,x):
    f3=a*x**3+b*x**2+c*x+d
    return f3

def main():
    x = np.linspace(-20, 20, 200)
    y1 = PTB3(2, -3, 5, -9, x)
    y2 = PTB2(-2, -5, 3, x)
    y3 = PTB1(-5, 2, x)
    fig, ax = d.subplots()
    ax.plot(x, y1, label=r'$2x^{3}-3x^{2}=5x-9$')
    ax.plot(x, y2, label=r'$-2x^{2}-5x+3$')
    ax.plot(x, y3, label=r'$-5x+2$')
    ax.set_xlabel('Truc hoanh - x')
    ax.set_ylabel('Truc tung - y')
    ax.set_title('bai1')
    ax.legend()
    d.show()
if __name__=='__main__':
    main()