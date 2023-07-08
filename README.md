# Cloud-Detection-Project

1.	Satellite Dataset - Training and Evaluation Unet1.ipynb
2.	Changing Custom images (imgs-converted.zip) format to Kaggle dataset format Unet2.ipynb 
3.	Testing on Custom 20 images
4.	Adding Custom 20 images to dataset - Training and evaluation Unet3.ipynb
5.	Finding new Cloud Dataset
6.	Creating Ground truth images of new Dataset according to Kaggle dataset format grounftruthconversion.py
7.	New Cloud dataset - Training and Evaluation Unet4.ipynb
8.	Adding Cloud dataset (CloudDataset.zip) into Satellite dataset - Training and Evaluation Unet5.ipynb
9.	Testing on New Cloud Dataset Test Images

### Dataset:

https://www.kaggle.com/code/cordmaur/38-cloud-simple-unet/data 

- 8400 training patches of size 384x384 (4 channels)
- 9201 patches for testing

New Dataset: SWINySeg- Singapore Whole sky Nychthemeron Image SEGmentation Database

### Dataset Pre-processing:
A multi-channel dataset for satellite images 
import Kaggle.json file, download it from your Kaggle account (See Unet1.ipynb)

https://medium.com/analytics-vidhya/how-to-create-a-custom-dataset-loader-in-pytorch-from-scratch-for-multi-band-satellite-images-c5924e908edf 

Other preprocessing code is provided in folder

### Model:
![model](https://github.com/eishaarif19/Cloud-Detection-Project/assets/63068028/171c253c-737b-4783-9db7-3f447747a652)
 
### Training and Validation:

https://medium.com/analytics-vidhya/creating-a-very-simple-u-net-model-with-pytorch-for-semantic-segmentation-of-satellite-images-223aa216e705 

- Batch Size: 12
- Epochs: 50
- Train – Validation Split: 6000 - 2400

### Results:
 ![r1](https://github.com/eishaarif19/Cloud-Detection-Project/assets/63068028/ec7674e3-f78f-4b85-ae46-932b4f7ca03e)
![r2](https://github.com/eishaarif19/Cloud-Detection-Project/assets/63068028/db034431-eae2-4564-9ec4-32258e17db15)
![r3](https://github.com/eishaarif19/Cloud-Detection-Project/assets/63068028/30ff614a-182b-4af9-81c0-158675a97a8d)
![r4](https://github.com/eishaarif19/Cloud-Detection-Project/assets/63068028/d016d5d8-c533-4fdf-96dc-5b79e3ef8864)

 
#### Accuracy: 95.35%
