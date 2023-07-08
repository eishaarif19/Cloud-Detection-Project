import cv2
import numpy as np
import os
import glob


path = "C:\\Users\\Eisha\\Desktop\\SINES internship\\Unet\\CloudDataset\\training\\images\\*.jpg"

# Load images
for img in glob.glob(path):

    os.remove(img)
