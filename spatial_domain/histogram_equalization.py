import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import SpatialTransforms as st

# Open image and convert to array
img = im.open('base_img.bmp')
img_array = np.asarray(img)

# Obtain equalized image and original and equalized histograms
img_eq_array, hist_equalized, hist_original = st.histogram_equalization(img_array)
img_eq = im.fromarray(img_eq_array)

# Apply equalization to the already equalized image
img_eq_array_twice, _, _ = st.histogram_equalization(img_eq_array)
img_eq_twice = im.fromarray(img_eq_array_twice)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.bar(range(256),hist_original)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.bar(range(256),hist_equalized)

# Create figure 3
fig3 = plt.figure(3)
ax3 = fig3.subplots()
ax3.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 4
fig4 = plt.figure(4)
ax4 = fig4.subplots()
ax4.imshow(img_eq, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 5
fig5 = plt.figure(5)
ax5 = fig5.subplots()
ax5.imshow(img_eq, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()

