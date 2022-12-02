import Bai2
import bai1
import matplotlib.pyplot as d
import numpy as np

def main():
    fig,(ax1,ax2)=d.subplots(1,2)
    x=np.linspace(-20,20,200)
    y1=bai1.PTB3(2,-3,5,-9,x)
    y2=bai1.PTB2(-2,-5,3,x)
    y3=bai1.PTB1(-5,3,x)
    y4=Bai2.ham1(x)
    y5=Bai2.ham2(x)
    ax1.plot(x,y1,label=r'$duong1$')
    ax1.plot(x,y2,label=r'$duong2$')
    ax1.plot(x,y3,label=r'$duong3$')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    ax2.plot(x,y4,label='r$duong4$')
    ax2.plot(x,y5,label=r'$duong5$')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.legend()
    d.show()
if __name__=='__main__':
    main()
