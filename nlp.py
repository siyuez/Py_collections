import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# define new callback rules
# class myCallback(tf.keras.callbacks.Callback):
# 	def on_epoch_end(self, epoch, logs={}):
# 		if(logs.get('loss')<0.4):
# 			print("\nLoss is low so cancelling training!")
# 			self.model.stop_training = True

# callbacks = myCallback()

sentences = [
	'I love my dog',
	'I love my cat',
	'Do you think my dog is amazing?'
]

# OOV - out of vocabulary
tokenizer = Tokenizer(num_words = 100, oov_token='<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

test_data = [
	'i really love my dog',
	'my dog loves my mantee',
]

sequences = tokenizer.texts_to_sequences(sentences)

padded =  pad_sequences(sequences, padding='post')
print(word_index)
print(sequences)
print(padded)

padded =  pad_sequences(sequences, padding='post', maxlen = 3)
print(padded)
