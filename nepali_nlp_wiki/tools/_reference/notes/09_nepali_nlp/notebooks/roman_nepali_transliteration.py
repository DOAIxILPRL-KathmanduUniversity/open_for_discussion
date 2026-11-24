import numpy as np
import pandas as pd
from datasets import load_dataset
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding
import tensorflow as tf

# --- 1. CONFIG & HYPERPARAMETERS ---
BATCH_SIZE = 64
EPOCHS = 20
LATENT_DIM = 128

# --- 2. DATA PREPARATION ---
try:
    dataset = load_dataset("Saugatkafley/Nepali-Roman-Transliteration")
    data = dataset['train'].to_pandas()
except:
    data = pd.DataFrame({'native word': ['नमस्ते'], 'english word': ['namaste']})

input_texts = data['english word'].astype(str).values
target_texts = ['\t' + str(text) + '\n' for text in data['native word'].values]

input_chars = sorted(list(set(''.join(input_texts)))) + ['<PAD>']
target_chars = sorted(list(set(''.join(target_texts)))) + ['<PAD>']
input_token_index = {char: i for i, char in enumerate(input_chars)}
target_token_index = {char: i for i, char in enumerate(target_chars)}
reverse_target_char_index = {i: char for char, i in target_token_index.items()}

# --- 3. MODEL ARCHITECTURE ---
encoder_inputs = Input(shape=(None,))
enc_emb = Embedding(len(input_chars), LATENT_DIM)(encoder_inputs)
_, state_h, state_c = LSTM(LATENT_DIM, return_state=True)(enc_emb)
encoder_states = [state_h, state_c]

decoder_inputs = Input(shape=(None,))
dec_emb_layer = Embedding(len(target_chars), LATENT_DIM)
dec_emb = dec_emb_layer(decoder_inputs)
decoder_lstm = LSTM(LATENT_DIM, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(dec_emb, initial_state=encoder_states)
decoder_dense = Dense(len(target_chars), activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# --- 4. DATA GENERATOR (SIMPLIFIED) ---
# Note: In a real scenario, use tf.data for large datasets
def generate_data(input_texts, target_texts):
    max_enc = max(len(t) for t in input_texts)
    max_dec = max(len(t) for t in target_texts)
    enc_in = np.zeros((len(input_texts), max_enc))
    dec_in = np.zeros((len(input_texts), max_dec))
    dec_tar = np.zeros((len(input_texts), max_dec, len(target_chars)))
    
    for i, (it, tt) in enumerate(zip(input_texts, target_texts)):
        for t, char in enumerate(it): enc_in[i, t] = input_token_index[char]
        for t, char in enumerate(tt):
            dec_in[i, t] = target_token_index[char]
            if t > 0: dec_tar[i, t-1, target_token_index[char]] = 1.0
    return enc_in, dec_in, dec_tar

# --- 5. INFERENCE ---
encoder_model = Model(encoder_inputs, encoder_states)
def transliterate(word):
    # Simplified inference logic
    pass 
