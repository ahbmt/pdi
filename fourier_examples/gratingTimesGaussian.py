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

# Create a grating pattern
wavelength = 200
grating = np.cos(2 * np.pi * X / wavelength)*np.cos(2 * np.pi * Y / wavelength)

# Calculate Fourier transform of grating
ft_gaussian = np.fft.ifftshift(gaussian)
ft_gaussian = np.fft.fft2(ft_gaussian)
ft_gaussian = np.fft.fftshift(ft_gaussian)

# Calculate Fourier transform of grating
ft_grating = np.fft.ifftshift(grating)
ft_grating = np.fft.fft2(ft_grating)
ft_grating = np.fft.fftshift(ft_grating)

# Fourier transform of convolution
ft_convolution = ft_grating * ft_gaussian

# Convolution in time
convolution = np.fft.ifftshift(ft_convolution)
convolution = np.fft.ifft2(convolution)
convolution = np.fft.fftshift(convolution)

#Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(gaussian, cmap='coolwarm')

#Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(grating, cmap='coolwarm')

# Creatre figure 3
fig3 = plt.figure(3)
ax3 = fig3.subplots()
ax3.imshow(abs(ft_gaussian), cmap='coolwarm')
ax3.set_xlim([480, 520])
ax3.set_ylim([520, 480]) # Note, order is reversed for y

# Creatre figure 4
fig4 = plt.figure(4)
ax4 = fig4.subplots()
ax4.imshow(abs(ft_grating), cmap='coolwarm')
ax4.set_xlim([480, 520])
ax4.set_ylim([520, 480]) # Note, order is reversed for y

# Creatre figure 5
fig5 = plt.figure(5)
ax5 = fig5.subplots()
ax5.imshow(abs(ft_convolution), cmap='coolwarm')
ax5.set_xlim([480, 520])
ax5.set_ylim([520, 480]) # Note, order is reversed for y

#Create figure 6
fig6 = plt.figure(6)
ax6 = fig6.subplots()
ax6.imshow(abs(convolution), cmap='coolwarm')

plt.show()