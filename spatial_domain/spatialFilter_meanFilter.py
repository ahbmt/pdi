import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import SpatialTransforms as st

# Open image and convert to array
img = im.open('base_img.bmp')
img_array = np.asarray(img)

# Obtain filtered image
img_mean_array = st.mean_filter(img_array,mask_size=5,slower=False)
img_mean = im.fromarray(img_mean_array)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_mean, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
