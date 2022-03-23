import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color
from scipy import io as sio

for i in range(10):

    if i+1 != 4:
        # Read files with color channel
        L = sio.loadmat(f'D:\Projects\study\Image\Image {i+1}\Image {i+1} - L.mat')['image_L']
        a = sio.loadmat(f'D:\Projects\study\Image\Image {i+1}\Image {i+1} - a.mat')['image_a']
        b = sio.loadmat(f'D:\Projects\study\Image\Image {i+1}\Image {i+1} - b.mat')['image_b']

        # Zip 3 color channels in 1 image
        lab_zip = np.dstack((L,a,b))
        lab_zip = color.lab2rgb(lab_zip)

        # Visualization of the read files and the result
        # fig, ax = plt.subplots(1, 4, figsize=(20, 20), sharex=True, sharey=True)
        # ax[0].imshow(L)
        # ax[1].imshow(a)
        # ax[2].imshow(b)
        # ax[3].imshow(lab_zip)

        # Save output
        io.imsave(f'reimage_{i+1}.jpg', (lab_zip*255).astype(np.uint8))