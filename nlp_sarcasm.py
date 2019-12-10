import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

vocab_size = 1000
embedding_dim = 64
max_length = 32
trunc_type = 'post'
padding_type = 'post'
oov_tok = "<OOV>"
training_size = 15000

import json

with open("sarcasm.json", 'r') as f:
	datastore = json.load(f)

sentences = []
labels = []
urls = []

for item in datastore:
	sentences.append(item['headline'])
	labels.append(item['is_sarcastic'])
	urls.append(item['article_link'])

training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
training_labels = labels[0:training_size]
testing_labels = labels[training_size:]

training_labels = np.array(training_labels)
testing_labels = np.array(testing_labels)

tokenizer = Tokenizer(num_words = vocab_size, oov_token='<OOV>')
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

model = tf.keras.Sequential([
	tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
	tf.keras.layers.GlobalAveragePooling1D(),
	tf.keras.layers.Dense(24, activation='relu'),
	tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
	loss='binary_crossentropy',
	optimizer='adam',
	metrics=['acc']
)

model.summary()

num_epochs = 30

history = model.fit(training_padded, training_labels, epochs=num_epochs, validation_data=(testing_padded, testing_labels), verbose=2)

import matplotlib.pyplot as plt

def plot_graphs(history, string):
	plt.plot(history.history[string])
	plt.plot(history.history['val_'+string])
	plt.xlabel('Epochs')
	plt.ylabel(string)
	plt.legend([string, 'val_'+string])
	plt.show()

plot_graphs(history,'acc')
plot_graphs(history,'loss')