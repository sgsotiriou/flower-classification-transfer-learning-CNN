# flower-classification-transfer-learning-CNN

## Contents

This repository contains two jupyter notebooks in the folder 'src'. The first one contains code that builds and then optimizes a CNN model for the classification of a dataset that contains a class of 104 types of flowers based on their images drawn from five different public datasets. The link to the dataset can be found in the notebook.

The second notebook employs transfer learning methods in order to classify a different dataset of flower images that contains about 65.000 images.

The repo also contains a demo code that allows the user to test various images on the optimized model from the first notebook.

## Requirements

The file 'requirements.txt' contains a full list of the requirements to run both the jupyter notebooks and the 'demo.py' file that contains the demonstration code.

## How to run the models

In order to run the notebooks it is recommended to use Kaggle's platform for running ML and DL code, enabling the usage of GPU. The jupyter notebooks were executed in that environment so in order to run them locally or in another platform, the train_dir and val_dir should be adjusted accordingly.

## How to test your own Images

The code 'demo.py' contains a code that lets the user test images of his choice using the best optimized model.

The code runs from the command line. When in the same folder as the 'demo.py' file, run the command 'python demo.py <image_location>' replace the <image_location> with the path to the image you want to check. The model tests the image and outputs a prediction on the command line.