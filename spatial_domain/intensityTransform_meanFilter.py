import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

def mean_filter(img_array,mask_size):

    # Mask parameters
    pad_width = int((mask_size-1)/2)
    weight = 1/(mask_size**2)
    mask = weight*np.ones((mask_size,mask_size))

    # Pad image array with zeroes at borders
    img_array_pad = np.pad(img_array,
                            ((pad_width,pad_width),),
                            mode='constant',
                            constant_values=((0,0),))
    
    # Create zeroes matrix for output
    rows_pad = np.shape(img_array_pad)[0]
    columns_pad = np.shape(img_array_pad)[1]
    img_array_out = np.zeros((rows_pad,columns_pad))

    # Set approach
    slower = False

    # Slower approach
    if slower:
        for i in range(pad_width,rows_pad-pad_width):
            for j in range(pad_width,columns_pad-pad_width):
                for k in range(-pad_width,1+pad_width):
                    for l in range(-pad_width,1+pad_width):
                        img_array_out[i][j] += img_array_pad[i+k][j+l]*weight

    # Faster approach
    else:
        for i in range(pad_width,rows_pad-pad_width):
            for j in range(pad_width,columns_pad-pad_width):
                image_slice = img_array_pad[i-pad_width:i+pad_width+1,j-pad_width:j+pad_width+1]
                matrix_arrangement = np.multiply(image_slice,mask)
                img_array_out[i][j] = np.sum(matrix_arrangement)

    img_array_out = img_array_out[pad_width:rows_pad-pad_width,pad_width:columns_pad-pad_width]
    print(np.shape(img_array_out))
    return img_array_out

# Open image and convert to array
img = im.open('base_img.bmp')
img_array = np.asarray(img)
print(np.shape(img_array))

# Obtain filtered image
img_mean_array = mean_filter(img_array,
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
