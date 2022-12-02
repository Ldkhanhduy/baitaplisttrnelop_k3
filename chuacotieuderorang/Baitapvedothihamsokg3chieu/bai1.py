import numpy as np
import matplotlib.pyplot as d
from matplotlib import cm

def ham_Rastrigin( x, y):
    z = x**2 + y**2 - np.cos(12*x) - np.cos(18*y)
    return z
def main():
    x = np.linspace(-1,2,num=200)
    y = np.linspace(-2,5,num=200)
    x, y = np.meshgrid(x, y)
    z = ham_Rastrigin(x, y)
    fig, ax =d.subplots(subplot_kw={"projection":"3d"})
    Rastrigin = ax.plot_surface(x, y, z,cmap=cm.gist_heat_r,linewidth=0, antialiased=False)
    ax.set_zlim(0, 200)
    fig.colorbar(Rastrigin, shrink=0.5,aspect=5)
    d.show()
if __name__=='__main__':
    main()