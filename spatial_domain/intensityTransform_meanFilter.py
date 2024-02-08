import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

def mean_filter(img_array,rows,columns,mask_size):

    pad_width = int((mask_size-1)/2)
    img_array_pad = np.pad(img_array,
                            ((pad_width,pad_width),),
                            mode='constant',
                            constant_values=((0,0),))
    
    img_array_out = np.zeros((rows,columns))

    weight = 1/(mask_size**2)
    for i in range(rows):
        for j in range(columns):
            for k in range(-pad_width,1+pad_width):
                for l in range(-pad_width,1+pad_width):
                    img_array_out[i][j] += img_array_pad[i+k][j+l]*weight

    return img_array_out

# Open image and convert to array
img = im.open('base_img.bmp')
img_array = np.asarray(img)

img_mean_array = mean_filter(img_array,
                             np.shape(img_array)[0],
                             np.shape(img_array)[1],
                             mask_size=5)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_mean_array, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
