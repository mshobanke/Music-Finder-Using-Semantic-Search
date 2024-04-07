#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import nltk
from nltk import word_tokenize
nltk.download('averaged_perceptron_tagger')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.corpus import stopwords

def lyric_data(song_lyrics):
    unique_sent = list(set(song_lyrics.splitlines()))

    # remove all words in brackets and compound words
    pattern = r'\([^)]*\)'
    pattern_comp = r'\b\w+-\w+\b'

    clean_text = []

    for sent in unique_sent:
        no_brack_sent = re.sub(pattern, '', sent)
        no_comp_sent = re.sub(pattern_comp, '', no_brack_sent)

        clean_text.append(no_comp_sent)

    # remove square brackets
    no_square = [sent_ for sent_ in clean_text if '[' not in sent_ and len(sent_) > 0 and 'Embed' not in sent_ and 'contributor' not in sent_]

    # remove blank space
    no_square = [i.strip() for i in no_square if len(i) > 0 and i.isspace() == False]

    return list(set(no_square))

def text_processing(lyric_sent):
     # change all lyric sentences into lower case
    lyric_sent = lyric_sent.lower()

    # remove punctuation marks
    no_punct = r"[^\w\s']"
    lyric_sent = re.sub(no_punct, '', lyric_sent)

    # remove stopwords
    stop_words = set(stopwords.words('english'))
    #stop_words.update(['yeah', 'woo', 'yo', 'mmm'])

    # tokenize and remove stopwords
    tokens = lyric_sent.split()
    tokens = [token for token in tokens if token not in stop_words]

    # change list back to string
    processed_lyric = ' '.join(tokens)

    return processed_lyric

def lyric_compiler(song_lyrics):
    lyric_list = lyric_data(song_lyrics)
    compiled_list = [' '.join(lyric_list[i:i+3]) for i in range(0, len(lyric_list), 3)]
    compiled_list = [text_processing(i) for i in compiled_list]
    return compiled_list