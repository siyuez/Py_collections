import tensorflow as tf
import numpy as np
from tensorflow import keras

# define new callback rules
class myCallback(tf.keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs={}):
		if(logs.get('loss')<0.4):
			print("\nLoss is low so cancelling training!")
			self.model.stop_training = True


callbacks = myCallback()

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

# import matplotlib.pyplot as plt
# plt.imshow(training_images[0])
# print(training_labels[0])
# print(training_images[0])

training_images  = training_images / 255.0  # normalization of grey scale point
test_images = test_images / 255.0

model = keras.Sequential([
	keras.layers.Flatten(input_shape=(28, 28)),
	keras.layers.Dense(128, activation=tf.nn.relu),
	keras.layers.Dense(10, activation=tf.nn.softmax)
])


model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])

model.evaluate(test_images, test_labels)