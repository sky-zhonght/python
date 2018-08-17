import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)
plt.contourf(X,Y,f(X,Y),20,cmap=plt.get_cmap("rainbow"))
c=plt.contour(X,Y,f(X,Y),20,cmap="bone")
plt.clabel(c)
plt.xticks(())
plt.yticks(())
plt.show()
