from keras.models import load_model
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout, Embedding, Masking
from keras.optimizers import Adam
from keras.utils import Sequence
from keras.preprocessing.text import Tokenizer

from sklearn.utils import shuffle

from IPython.display import HTML

from itertools import chain
from keras.utils import plot_model
import numpy as np
import pandas as pd
import random
import json
import re

RANDOM_STATE = 50
TRAIN_FRACTION = 0.7


def get_model(model_name):
    """Retrieve a Keras model and embeddings"""
    model = load_model(f'../models/{model_name}.h5')
    embeddings = model.get_layer(index = 0)
    embeddings = embeddings.get_weights()[0]
    embeddings = embeddings / np.linalg.norm(embeddings, axis = 1).reshape((-1, 1))
    embeddings = np.nan_to_num(embeddings)
    word_idx = []
    with open(f'../data/training-rnn.json', 'rb') as f:
        for l in f:
            word_idx.append(json.loads(l))
        
    word_idx = word_idx[0]
    word_idx['UNK'] = 0
    idx_word = {index: word for word, index in word_idx.items()}
    return model, embeddings, word_idx, idx_word

def get_embeddings(model):
    """Retrieve the embeddings in a model"""
    embeddings = model.get_layer(index = 0)
    embeddings = embeddings.get_weights()[0]
    embeddings = embeddings / np.linalg.norm(embeddings, axis = 1).reshape((-1, 1))
    embeddings = np.nan_to_num(embeddings)
    return embeddings
    
def find_closest(query, embedding_matrix, word_idx, idx_word, n = 10):
    """Find closest words to a query word in embeddings"""
    
    idx = word_idx.get(query, None)
    # Handle case where query is not in vocab
    if idx is None:
        print(f'{query} not found in vocab.')
        return
    else:
        vec = embedding_matrix[idx]
        # Handle case where word doesn't have an embedding
        if np.all(vec == 0):
            print(f'{query} has no pre-trained embedding.')
            return
        else:
            # Calculate distance between vector and all others
            dists = np.dot(embedding_matrix, vec)
            
            # Sort indexes in reverse order
            idxs = np.argsort(dists)[::-1][:n]
            sorted_dists = dists[idxs]
            closest = [idx_word[i] for i in idxs]
            
    print(f'Query: {query}\n')
    # Print out the word and cosine distances
    for word, dist in zip(closest, sorted_dists):
        print(f'Word: {word:15} Cosine Similarity: {round(dist, 4)}')
        
def format_sequence(s):
    """Add spaces around punctuation and remove references to images/citations."""
    
    # Add spaces around punctuation
    s =  re.sub(r'(?<=[^\s0-9])(?=[.,;?])', r' ', s)
    
    # Remove references to figures
    s = re.sub(r'\((\d+)\)', r'', s)
    
    # Remove double spaces
    s = re.sub(r'\s\s', ' ', s)
    return s

def remove_spaces(s):
    """Remove spaces around punctuation"""
    s = re.sub(r'\s+([.,;?])', r'\1', s)
    
    return s


def get_data(file, filters='!"%;[\\]^_`{|}~\t\n', training_len=50,
             lower=False):
    """Retrieve formatted training and validation data from a file"""
    
    data = pd.read_csv(file, parse_dates=['patent_date']).dropna(subset = ['patent_abstract'])
    abstracts = [format_sequence(a) for a in list(data['patent_abstract'])]
    word_idx, idx_word, num_words, word_counts, texts, sequences, features, labels = make_sequences(
        abstracts, training_len, lower, filters)
    X_train, X_valid, y_train, y_valid = create_train_valid(features, labels, num_words)
    training_dict = {'X_train': X_train, 'X_valid': X_valid, 
                     'y_train': y_train, 'y_valid': y_valid}
    return training_dict, word_idx, idx_word, sequences

def create_train_valid(features,
                       labels,
                       num_words,
                       train_fraction=0.7):
    """Create training and validation features and labels."""
    
    # Randomly shuffle features and labels
    features, labels = shuffle(features, labels, random_state=RANDOM_STATE)

    # Decide on number of samples for training
    train_end = int(train_fraction * len(labels))

    train_features = np.array(features[:train_end])
    valid_features = np.array(features[train_end:])

    train_labels = labels[:train_end]
    valid_labels = labels[train_end:]

    # Convert to arrays
    X_train, X_valid = np.array(train_features), np.array(valid_features)

    # Using int8 for memory savings
    y_train = np.zeros((len(train_labels), num_words), dtype=np.int8)
    y_valid = np.zeros((len(valid_labels), num_words), dtype=np.int8)

    # One hot encoding of labels
    for example_index, word_index in enumerate(train_labels):
        y_train[example_index, word_index] = 1

    for example_index, word_index in enumerate(valid_labels):
        y_valid[example_index, word_index] = 1

    # Memory management
    import gc
    gc.enable()
    del features, labels, train_features, valid_features, train_labels, valid_labels
    gc.collect()

    return X_train, X_valid, y_train, y_valid

def make_sequences(texts, training_length = 50,
                   lower = True, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'):
    """Turn a set of texts into sequences of integers"""
    
    # Create the tokenizer object and train on texts
    tokenizer = Tokenizer(lower=lower, filters=filters)
    tokenizer.fit_on_texts(texts)
    
    # Create look-up dictionaries and reverse look-ups
    word_idx = tokenizer.word_index
    idx_word = tokenizer.index_word
    num_words = len(word_idx) + 1
    word_counts = tokenizer.word_counts
    
    print(f'There are {num_words} unique words.')
    
    # Convert text to sequences of integers
    sequences = tokenizer.texts_to_sequences(texts)
    
    # Limit to sequences with more than training length tokens
    seq_lengths = [len(x) for x in sequences]
    over_idx = [i for i, l in enumerate(seq_lengths) if l > (training_length + 20)]
    
    new_texts = []
    new_sequences = []
    
    # Only keep sequences with more than training length tokens
    for i in over_idx:
        new_texts.append(texts[i])
        new_sequences.append(sequences[i])
        
    features = []
    labels = []
    
    # Iterate through the sequences of tokens
    for seq in new_sequences:
        
        # Create multiple training examples from each sequence
        for i in range(training_length, len(seq)):
            # Extract the features and label
            extract = seq[i - training_length: i + 1]
            
            # Set the features and label
            features.append(extract[:-1])
            labels.append(extract[-1])
    
    print(f'There are {len(features)} sequences.')
    
    # Return everything needed for setting up the model
    return word_idx, idx_word, num_words, word_counts, new_texts, new_sequences, features, labels



def header(text, color = 'black', gen_text = None):
    if gen_text:
        raw_html = f'<h1 style="color: {color};"><p><center>' + str(
        text) + '<span style="color: red">' + str(gen_text) + '</center></p></h1>'
    else:
        raw_html = f'<h1 style="color: {color};"><center>' + str(
            text) + '</center></h1>'
    return raw_html


def box(text, gen_text=None):
    if gen_text:
        raw_html = '<div style="border:1px inset black;padding:1em;font-size: 20px;"> <p>' + str(
            text) +'<span style="color: red">' + str(gen_text) + '</p></div>'

    else:
        raw_html = '<div style="border:1px inset black;padding:1em;font-size: 20px;">' + str(
            text) + '</div>'
    return raw_html


def addContent(old_html, raw_html):
    old_html += raw_html
    return old_html

def seed_sequence(model, s, word_idx, idx_word, 
                  diversity = 0.75, num_words = 50):
    """Generate output starting from a seed sequence."""
    # Original formated text
    start = format_sequence(s).split()
    gen = []
    s = start[:]
    # Generate output
    for _ in range(num_words):
        # Conver to arry
        x = np.array([word_idx.get(word, 0) for word in s]).reshape((1, -1))

        # Make predictions
        preds = model.predict(x)[0].astype(float)

        # Diversify
        preds = np.log(preds) / diversity
        exp_preds = np.exp(preds)
        # Softmax
        preds = exp_preds / np.sum(exp_preds)
        # Pick next index
        next_idx = np.argmax(np.random.multinomial(1, preds, size = 1))
        s.append(idx_word[next_idx])
        gen.append(idx_word[next_idx])
    
    # Formatting in html
    start = remove_spaces(' '.join(start)) + ' '
    gen = remove_spaces(' '.join(gen)) 
    html = ''
    html = addContent(html, header('Input Seed ', color = 'black', gen_text = 'Network Output'))
    html = addContent(html, box(start, gen))
    return html

   
def make_sequences_new(texts,
                   training_length=50,
                   lower=True,
                   filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'):
    """Turn a set of texts into sequences of integers"""

    # Create the tokenizer object and train on texts
    tokenizer = Tokenizer(lower=lower, filters=filters)
    tokenizer.fit_on_texts(texts)

    # Convert text to sequences of integers
    sequences = tokenizer.texts_to_sequences(texts)

    # Limit to sequences with more than (training length + 20) tokens
    seq_lengths = [len(x) for x in sequences]
    over_idx = [
        i for i, l in enumerate(seq_lengths) if l > (training_length + 20)
    ]

    new_texts = []

    # Only keep sequences with more than training length tokens
    for i in over_idx:
        new_texts.append(texts[i])
    
    tokenizer = Tokenizer(lower=lower, filters=filters)
    # Refit on long texts
    tokenizer.fit_on_texts(new_texts)
    new_sequences = tokenizer.texts_to_sequences(new_texts)
    
    # Create look-up dictionaries and reverse look-ups
    word_idx = tokenizer.word_index
    idx_word = tokenizer.index_word
    num_words = len(word_idx) + 1
    word_counts = tokenizer.word_counts

    print(f'There are {num_words} unique words.')

    features = []
    labels = []

    # Iterate through the sequences of tokens
    for seq in new_sequences:

        # Create multiple training examples from each sequence
        for i in range(training_length, len(seq)):
            # Extract the features and label
            extract = seq[i - training_length:i + 1]

            # Set the features and label
            features.append(extract[:-1])
            labels.append(extract[-1])

    print(f'There are {len(features)} training sequences.')

    # Return everything needed for setting up the model
    return word_idx, idx_word, num_words, word_counts, new_texts, new_sequences, features, labels