import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import SpatialTransforms as st

# Open image and convert to array
img = im.open('base_img_equalized.bmp')
img_array = np.asarray(img)

# Apply s&p noise to image
img_sp_array = st.salt_and_pepper(img_array,threshold=0.05)
img_sp = im.fromarray(img_sp_array)

# Obtain filtered image (median)
img_median_array = st.median_filter(img_sp_array,mask_size=5)
img_median = im.fromarray(img_median_array)

# Obtain filtered image (mean)
img_mean_array = st.mean_filter(img_sp_array,mask_size=5,slower=False)
img_mean = im.fromarray(img_mean_array)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_sp, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 3
fig3 = plt.figure(3)
ax3 = fig3.subplots()
ax3.imshow(img_median, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 4
fig4 = plt.figure(4)
ax4 = fig4.subplots()
ax4.imshow(img_mean, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
