import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import SpatialTransforms as st

# Open image and convert to array
img = im.open('base_img_equalized.bmp')
img_array = np.asarray(img)

# Obtain filtered image - x axis
img_sobel_x_array = st.sobel_x(img_array,adjusted=False)
img_sobel_x = im.fromarray(img_sobel_x_array)

# Obtain filtered image - y axis
img_sobel_y_array = st.sobel_y(img_array,adjusted=False)
img_sobel_y = im.fromarray(img_sobel_y_array)

# Composite image
img_sobel_array = img_sobel_x_array + img_sobel_y_array
img_sobel = im.fromarray(img_sobel_array)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_sobel_x, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 3
fig3 = plt.figure(3)
ax3 = fig3.subplots()
ax3.imshow(img_sobel_y, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 4
fig4 = plt.figure(4)
ax4 = fig4.subplots()
ax4.imshow(img_sobel, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
