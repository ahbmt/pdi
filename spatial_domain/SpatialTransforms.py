import numpy as np

def _operation_variables(img_array):

    # Get the number of rows and columns
    rows = np.shape(img_array)[0]
    columns = np.shape(img_array)[1]
    
    # Create an empty image of appropriate size
    img_array_out = np.zeros((rows,columns))

    return img_array_out, rows, columns

def _histogram(img_array):

    # Get the image dimensions
    _, rows, columns = _operation_variables(img_array)

    # Create the output histogram
    hist_out = np.zeros(256)

    # Calculate the histogram values
    for i in range(rows):
        for j in range(columns):
            hist_out[int(img_array[i][j])] += 1

    return hist_out

# Convolution with a given mask
def _mask_convolution(img_array,mask):

    # Pad array w/ 0 to appropriate dimensions
    pad_width = int((np.shape(mask)[0]-1)/2)

    img_array = np.pad(img_array,
                       ((pad_width,pad_width),),
                        mode='constant',
                        constant_values=((0,0),))

    # Get dimensions and output array
    img_array_out, rows_pad, columns_pad = _operation_variables(img_array)

    # Convolution of mask with input image
    for i in range(pad_width,rows_pad-pad_width):
            for j in range(pad_width,columns_pad-pad_width):
                image_slice = img_array[i-pad_width:i+pad_width+1,
                                        j-pad_width:j+pad_width+1]
                matrix_arrangement = np.multiply(image_slice,mask)
                img_array_out[i][j] = np.sum(matrix_arrangement)

    return img_array_out[pad_width:rows_pad-pad_width,
                         pad_width:columns_pad-pad_width]

# Negative intensity transformation
def negative_transform(img_array):

    # Get dimensions and output array
    img_array_out, rows, columns = _operation_variables(img_array)

    # Obtain negative transform
    for i in range(rows):
        for j in range(columns):
            img_array_out[i][j] = 255 - img_array[i][j]

    return img_array_out

# Binary intensity transformation
def bit_slice(img_array,intensity):

    # Get dimensions and output array
    img_array_out, rows, columns = _operation_variables(img_array)

    # Obtain bit slice
    for i in range(rows):
        for j in range(columns):
            if img_array[i][j] > intensity:                
                img_array_out[i][j] = 255
            else:
                img_array_out[i][j] = 0

    return img_array_out

# pow intensity transformation
def pow_transform(img_array,constant,gamma):

    # Get dimensions and output array
    img_array_out, rows, columns = _operation_variables(img_array)

    # Calculate power transform
    for i in range(rows):
        for j in range(columns):
            if np.rint(constant*np.power(img_array[i][j],gamma)) > 255:
                img_array_out[i][j] = 255
            else:
                img_array_out[i][j] = np.rint(constant*np.power(img_array[i][j],gamma))
            
    return img_array_out

# log intensity transformation
def log_transform(img_array,constant):
    
    # Get dimensions and output array
    img_array_out, rows, columns = _operation_variables(img_array)

    for i in range(rows):
        for j in range(columns):
            img_array_out[i][j] = np.rint(constant*np.log10(1+img_array[i][j]))
            
    return img_array_out

# Uniform mean spatial filter
def mean_filter(img_array,mask_size,slower):

    # Slower approach
    if slower:
         # Mask parameters
        weight = 1/(mask_size**2)
        pad_width = int((mask_size-1)/2)

        # Pad image array with zeroes at borders
        img_array_pad = np.pad(img_array,
                            ((pad_width,pad_width),),
                            mode='constant',
                            constant_values=((0,0),))
    
        # Get dimensions and output array
        img_array_out, rows_pad, columns_pad = _operation_variables(img_array_pad)
    
        for i in range(pad_width,rows_pad-pad_width):
            for j in range(pad_width,columns_pad-pad_width):
                for k in range(-pad_width,1+pad_width):
                    for l in range(-pad_width,1+pad_width):
                        img_array_out[i][j] += img_array_pad[i+k][j+l]*weight

        # Adjust image size
        img_array_out = img_array_out[pad_width:rows_pad-pad_width,
                                      pad_width:columns_pad-pad_width]
    
    # Faster approach
    else:
        # Mask parameters
        weight = 1/(mask_size**2)
        mask = weight*np.ones((mask_size,mask_size))

        # Convolution
        img_array_out = _mask_convolution(img_array,mask)

    return img_array_out

# Histogram equalization
def histogram_equalization(img_array):

    # Get dimensions and output array
    img_array_out, rows, columns = _operation_variables(img_array)

    # Calculate normalization constant
    norm_cnt = 255/(rows*columns)

    # Obtain histogram of original image
    hist_original = _histogram(img_array)

    # Obtain equalized image
    for i in range(rows):
        for j in range(columns):
            cumulative_prob = np.sum(hist_original[0:int(img_array[i][j])])
            img_array_out[i][j] = np.rint(norm_cnt*cumulative_prob)

    # Obtain equalized histogram
    hist_equalized = _histogram(img_array_out)

    return img_array_out, hist_equalized, hist_original