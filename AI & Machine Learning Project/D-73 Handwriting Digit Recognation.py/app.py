import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
import matplotlib.pyplot as plt

# load the mnist dataset
mnist = tf.keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# Normalize pixel values (0-255) to (0-1) for better performance
X_train, X_test = X_train / 255.0, X_test / 255.0

# Display a sample digit
plt.imshow(X_train[0], cmap='gray')
plt.title(f"Label: {Y_train[0]}")
plt.show()
