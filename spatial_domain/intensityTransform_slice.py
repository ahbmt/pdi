import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
import SpatialTransforms as st

# Open image and convert to array
img = im.open('base_img.bmp')
img_array = np.asarray(img)

# Call the transform using the array and convert to image
img_array_binary = st.binary_transform(img_array,np.mean(img_array))
img_binary = im.fromarray(img_array_binary)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_binary, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
