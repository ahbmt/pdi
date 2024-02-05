import numpy as np
import matplotlib.pyplot as plt

# Set image field
X = np.arange(-500, 501, 1)
Y = np.arange(-500, 501, 1)
X, Y = np.meshgrid(X, Y)

# Create a gaussian pattern
sigma = 100
gaussian = (np.exp(-pow(X,2)/(2*pow(sigma,2)))
            *np.exp(-pow(Y,2)/(2*pow(sigma,2))))

# Calculate Fourier transform of gaussian
ft = np.fft.ifftshift(gaussian)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)

#Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(gaussian, cmap='coolwarm')

# Creatre figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(abs(ft), cmap='coolwarm')
ax2.set_xlim([480, 520])
ax2.set_ylim([520, 480]) # Note, order is reversed for y

plt.show()