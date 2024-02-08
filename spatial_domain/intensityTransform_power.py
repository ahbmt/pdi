import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im

# pow intensity transformation
def pow_transform(img_array,rows,columns,constant,gamma):
    
    img_array_out = np.zeros((rows,columns))

    for i in range(rows):
        for j in range(columns):
            if np.rint(constant*np.power(img_array[i][j],gamma)) > 255:
                img_array_out[i][j] = 255
            else:
                img_array_out[i][j] = np.rint(constant*np.power(img_array[i][j],gamma))
            
    return img_array_out

# Open image and convert to array
img = im.open('base_img.bmp')
img_array = np.asarray(img)

# Call the transform using the array and convert to image (gamma>1)
img_array_pow_grt = pow_transform(img_array,
                                  np.shape(img_array)[0],
                                  np.shape(img_array)[1],
                                  constant=1,
                                  gamma=1.5)
img_pow_grt = im.fromarray(img_array_pow_grt)

# Call the transform using the array and convert to image (gamma<1)
img_array_pow_lwr = pow_transform(img_array,
                                  np.shape(img_array)[0],
                                  np.shape(img_array)[1],
                                  1,
                                  0.67)
img_pow_lwr = im.fromarray(img_array_pow_lwr)

# Gamma correction
img_array_pow_crt = pow_transform(img_array_pow_grt,
                                  np.shape(img_array)[0],
                                  np.shape(img_array)[1],
                                  1,
                                  0.67)
img_pow_crt = im.fromarray(img_array_pow_crt)

# Create figure 1
fig1 = plt.figure(1)
ax1 = fig1.subplots()
ax1.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 2
fig2 = plt.figure(2)
ax2 = fig2.subplots()
ax2.imshow(img_pow_grt, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 3
fig3 = plt.figure(3)
ax3 = fig3.subplots()
ax3.imshow(img_pow_lwr, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Create figure 4
fig4 = plt.figure(4)
ax4 = fig4.subplots()
ax4.imshow(img_pow_crt, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

# Show plots
plt.show()
