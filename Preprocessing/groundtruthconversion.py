import cv2
import numpy as np
import glob

path = "C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\DATASET\\swinyseg\\GTmaps\\*.png"

#C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\DATASET\\swimseg\\GTmaps\\*.png

# Load images
for img in glob.glob(path):
    
    im = cv2.imread(img)

    #Change size of image
    im = cv2. resize(im, (384, 384))

    #Convert yellow to white and black to purple
    im[np.all(im == (0, 0, 0), axis=-1)] = (128,0,128)
    im[np.all(im == (255, 255, 255), axis=-1)] = (0, 255,255)

    #print("size", im.shape)

    # Save result
    cv2.imwrite(img,im)
