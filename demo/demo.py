import tensorflow as tf
import numpy as np
from PIL import Image
import sys
import cv2
import argparse

# Load the saved model
model = tf.keras.models.load_model('../model/Model_with_L1L2_Regularization.h5', compile=False)
model.compile(loss="sparse_categorical_crossentropy",
             metrics=["accuracy"],
             optimizer="adam")

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Image classification prediction')
parser.add_argument('image_path', type=str, help='Path to the input image')
args = parser.parse_args()

# Read and preprocess the image
img = cv2.imread(args.image_path)
img = cv2.resize(img,(180,180))
img = np.reshape(img,[1,180,180,3])

prediction = model.predict(img)
predicted_class = np.argmax(prediction)

print(predicted_class)