import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

def intensity_transform(Z):
    
    Z_temp = Z
    for i in range(np.shape(Z)[0]):
        for j in range(np.shape(Z)[1]):
            if Z[i][j] <= 0:
                Z_temp[i][j] = -1
            elif Z[i][j] > 0:
                Z_temp[i][j] = 1

    return Z_temp


# Make data.
X = np.arange(0, 10, 0.25)
Y = np.arange(0, 10, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X)*np.sin(Y)

#Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
# Plot the surface in figure 1
surf1 = ax1.plot_surface(X, Y, Z, cmap='grey',
                       linewidth=0, antialiased=True)

# Customize the z axis in figure 1
ax1.set_zlim(np.min(Z), np.max(Z))
ax1.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax1.zaxis.set_major_formatter('{x:.02f}')

# Intensity transform
Ztf = intensity_transform(Z)

#Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection='3d')
# Plot the surface in figure 2
surf2 = ax2.plot_surface(X, Y, Ztf, cmap='grey',
                       linewidth=0, antialiased=True)

# Customize the z axis in figure 2
ax2.set_zlim(np.min(Ztf), np.max(Ztf))
ax2.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax2.zaxis.set_major_formatter('{x:.02f}')

# Show figures
plt.show()