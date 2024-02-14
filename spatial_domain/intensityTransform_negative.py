import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

# Negative intensity transformation
def negative_transform(img_array):

    rows = np.shape(img_array)[0]
    columns = np.shape(img_array)[1]
    
    img_array_out = np.zeros((rows,columns))

    for i in range(rows):
        for j in range(columns):
            img_array_out[i][j] = 255 - img_array[i][j]

    return img_array_out

# Open image and convert to array
img = im.open('base_img.bmp')
img_array = np.asarray(img)

# Call the transform using the array and convert to image
img_array_negative = negative_transform(img_array)
img_negative = im.fromarray(img_array_negative) 

print(np.max(img_array_negative))

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_negative, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
