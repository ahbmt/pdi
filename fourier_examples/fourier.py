import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator
from scipy.fft import fft2, fftfreq 

# Make data.
dS = 0.25
X = np.arange(-5, 5, dS)
Y = np.arange(-5, 5, dS)
X, Y = np.meshgrid(X, Y)

Xf = fftfreq(len(X), dS)
Yf = fftfreq(len(Y), dS)

Z = np.cos(X)*np.cos(Y)
Zf = fft2(Z)

#Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
# Plot the surface in figure 1
surf1 = ax1.plot_surface(X, Y, Z, cmap='coolwarm',
                       linewidth=0, antialiased=True)

# Customize the z axis in figure 1
ax1.set_zlim(np.min(Z), np.max(Z))
ax1.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax1.zaxis.set_major_formatter('{x:.02f}')

#Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection='3d')
# Plot the surface in figure 2
surf2 = ax2.plot_surface(Xf, Yf, np.abs(Zf), cmap='coolwarm',
                       linewidth=0, antialiased=True)

# Customize the z axis in figure 2
ax2.set_zlim(np.min(np.abs(Zf)), np.max(np.abs(Zf)))
ax2.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax2.zaxis.set_major_formatter('{x:.02f}')

# Show figures
plt.show()