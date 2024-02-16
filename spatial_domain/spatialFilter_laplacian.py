import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import SpatialTransforms as st

# Open image and convert to array
img = im.open('base_img_equalized.bmp')
img_array = np.asarray(img)

# Obtain filtered image
img_laplacian_array = st.laplacian_filter(img_array,adjusted=False)
img_laplacian = im.fromarray(img_laplacian_array)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_laplacian, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
