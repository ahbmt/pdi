import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import SpatialTransforms as st

# Open image and convert to array
img = im.open('base_img_equalized.bmp')
img_array = np.asarray(img)

# Call the transform using the array and convert to image (gamma>1)
img_array_pow_grt = st.pow_transform(img_array,constant=1,gamma=1.5)
img_pow_grt = im.fromarray(img_array_pow_grt)

# Call the transform using the array and convert to image (gamma<1)
img_array_pow_lwr = st.pow_transform(img_array,constant=1,gamma=0.67)
img_pow_lwr = im.fromarray(img_array_pow_lwr)

# Gamma correction
img_array_pow_crt = st.pow_transform(img_array_pow_grt,constant=1,gamma=0.67)
img_pow_crt = im.fromarray(img_array_pow_crt)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_pow_grt, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 3
fig3 = plt.figure(3)
ax3 = fig3.subplots()
ax3.imshow(img_pow_lwr, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 4
fig4 = plt.figure(4)
ax4 = fig4.subplots()
ax4.imshow(img_pow_crt, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
