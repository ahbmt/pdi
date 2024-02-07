import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

# Binary intensity transformation
def binary_transform(img_array,rows,columns):
    
    img_array_out = np.zeros((rows,columns))

    mean_intensity = np.mean(img_array)

    for i in range(rows):
        for j in range(columns):
            if img_array[i][j] > mean_intensity:                
                img_array_out[i][j] = 256
            else:
                img_array_out[i][j] = 0

    return img_array_out

# Open image and convert to array
img = im.open('cat.bmp')
img_array = np.asarray(img)

# Get image dimensions
rows = np.shape(img_array)[0]
columns = np.shape(img_array)[1]

# Call the transform using the array and convert to image
img_array_binary = binary_transform(img_array,rows,columns)
img_binary = im.fromarray(img_array_binary)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_binary, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)

# Show plots
plt.show()
