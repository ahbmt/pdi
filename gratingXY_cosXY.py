import numpy as np
import matplotlib.pyplot as plt

# Set image field
X = np.arange(-500, 501, 1)
Y = np.arange(-500, 501, 1)
X, Y = np.meshgrid(X, Y)

# Create a grating pattern
wavelength = 200
wo = (2*np.pi)/wavelength
grating = np.cos(wo*X*Y)

# Calculate Fourier transform of grating
ft = np.fft.ifftshift(grating)
ft = np.fft.fft2(ft)
ft = np.fft.fftshift(ft)

#Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(grating, cmap='coolwarm')

# Creatre figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(abs(ft), cmap='coolwarm')

plt.show()