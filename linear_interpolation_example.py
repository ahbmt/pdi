import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=11)
y = np.cos(-x**2 / 9.0)

xnew = np.linspace(0, 10, num=1001)
ynew = np.interp(xnew, x, y)

plt.plot(xnew, ynew, '-', label='Linear interpolation')
plt.plot(x, y, 'o', label='Data')
plt.legend(loc='best')
plt.show()