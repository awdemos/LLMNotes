# Import necessary libraries
from transformers import BertTokenizerFast, TFBertModel
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

# Load pre-trained BERT model and tokenizer
bert = TFBertModel.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")

# Define model parameters and architecture
max_length = 256
tokens = keras.layers.Input(shape=(max_length,), dtype=tf.int32)
masks = keras.layers.Input(shape=(max_length,), dtype=tf.int32)
embedding_layer = bert([tokens, masks])[0][:, 0, :]
dense = keras.layers.Dense(units=2, activation="softmax")(embedding_layer)
model = keras.Model([tokens, masks], dense)

# Compile the model
model.compile(optimizer="Adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()

# Load and preprocess the IMDB dataset
imdb_df = pd.read_csv("IMDB Dataset.csv")
reviews = list(imdb_df.review)
tokenized_reviews = tokenizer.batch_encode_plus(
    reviews,
    return_tensors="tf",
    max_length=max_length,
    truncation=True,
    padding='max_length'
)

# Split data into training and test sets
train_split = int(0.8 * len(tokenized_reviews["attention_mask"]))
train_tokens = tokenized_reviews["input_ids"][:train_split]
test_tokens = tokenized_reviews["input_ids"][train_split:]
train_masks = tokenized_reviews["attention_mask"][:train_split]
test_masks = tokenized_reviews["attention_mask"][train_split:]

# Prepare labels for training and testing
sentiments = list(imdb_df.sentiment)
labels = np.array([[0, 1] if sentiment == "positive" else [1, 0] for sentiment in sentiments])
train_labels = labels[:train_split]
test_labels = labels[train_split:]

# Train the model
model.fit([train_tokens, train_masks], train_labels, epochs=500)
