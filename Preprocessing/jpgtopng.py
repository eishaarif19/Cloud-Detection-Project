import cv2
import numpy as np
import os
import glob


path = "C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\CloudDataset\\training\\images\\*.jpg"

#C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\CloudDataset\\training\\images\\*.jpg


# Load images
for img in glob.glob(path):

    im = cv2.imread(img)
        
    fn, _ = os.path.splitext(img)

    file_extension = ".png"

    new_path = os.path.join(fn +file_extension )
    
    # Save result
    cv2.imwrite(new_path,im)
