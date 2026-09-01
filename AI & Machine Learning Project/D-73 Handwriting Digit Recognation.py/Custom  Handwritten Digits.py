import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense

# load the mnist dataset
mnist = tf.keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# Normalize pixel values (0-255) to (0-1) for better performance
X_train, X_test = X_train / 255.0, X_test / 255.0

# Reshape dataset for CNN input (batch_size, height, width, channels)
X_train_reshaped = X_train.reshape(-1, 28, 28, 1)
X_test_reshaped = X_test.reshape(-1, 28, 28, 1)

# Build the CNN model
model = Sequential([
    Input(shape=(28, 28, 1)),
    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax")
])

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(X_train_reshaped, Y_train, epochs=5, validation_data=(X_test_reshaped, Y_test))

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test_reshaped, Y_test)
print(f"\nTest Accuracy: {test_acc:.4f}")

# Select a test image
index = 0
test_image = X_test[index].reshape(1, 28, 28, 1)

# Predict Digit
predicted_label = model.predict(test_image)
plt.imshow(X_test[index], cmap="gray")
plt.title(f"Predicted: {np.argmax(predicted_label)}")
plt.axis("off")
plt.show()