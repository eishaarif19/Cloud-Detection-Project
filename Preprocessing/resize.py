import cv2
import numpy as np

import glob
path = "C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\CloudDataset\\training\\images\\*.jpg"

#C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\CloudDataset\\training\\train_gt\\*.png
#C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\CloudDataset\\testing\\test_gt\\*.png
#C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\CloudDataset\\training\\images\\*.png

# Load images
for img in glob.glob(path):
    
    im = cv2.imread(img)

    #Change size of image
    im = cv2. resize(im, (384, 384))
    #print(im.shape)

    # Save result
    cv2.imwrite(img,im)
