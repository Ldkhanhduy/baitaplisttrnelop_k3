import matplotlib.pyplot as d
import numpy as np

def ham1(x):
    f1=np.cos(x/np.pi)
    return f1
def ham2(x):
    f2=np.sin((np.pi*x)/3)
    return f2
def main():
    x=np.linspace(-20,20,200)
    y1=ham1(x)
    y2=ham2(x)
    fig,ax=d.subplots()
    ax.plot(x,y1,label=r'$Cos(x/pi)$')
    ax.plot(x,y2,label=r'$Sin((pi/3)x$')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Bai2')
    ax.legend()
    d.show()
if __name__=='__main__':
    main()