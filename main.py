import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

word_index=imdb.get_word_index()
reverse_word_index={value:key for key ,value in word_index.items()}
model=load_model('simple_rnn_imdb.h5')

# Step 2: Helper Functions

from tensorflow.keras.preprocessing import sequence

# Function to decode encoded reviews back to text
def decode_review(encoded_review):
    return ' '.join(
        reverse_word_index.get(i - 3, '?') for i in encoded_review
    )


# Function to preprocess user input text
def preprocess_text(text):
    # 1. Convert to lowercase and split into words
    words = text.lower().split()

    # 2. Convert words to integer indices
    #    2 = "unknown word" index in IMDB
    encoded_review = [word_index.get(word, 2) + 3 for word in words]

    # 3. Pad the sequence to match model input length
    padded_review = sequence.pad_sequences(
        [encoded_review],
        maxlen=500
    )

    return padded_review

def predict_sentiment(review):
    """
    Predict sentiment of a review
    """
    preprocessed_input = preprocess_text(review)
    
    prediction = model.predict(preprocessed_input, verbose=0)
    
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    
    return sentiment, float(prediction[0][0])

st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to classify it as positive or negative.")

# User input
user_input = st.text_area("Movie Review")

if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter a movie review.")
    else:
        preprocessed_input = preprocess_text(user_input)

        # Make prediction
        prediction = model.predict(preprocessed_input, verbose=0)
        score = float(prediction[0][0])

        sentiment = "Positive 😊" if score > 0.5 else "Negative 😞"

        # Display result
        st.subheader("Result")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Prediction Score:** {score:.4f}")