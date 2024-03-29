import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize,pos_tag
import numpy as np

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_seniority_level(years):
    """
    Determines the seniority level based on the number of years of experience.
    
    Parameters:
        years (int): The number of years of experience.
        
    Returns:
        str: The seniority level based on the number of years of experience.
            Possible values are 'Junior', 'Mid', 'Senior', or 'Expert'.
    """
    output = 'Expert'
    if years <= 3:
        output = 'Junior'
    else:
        if years <= 5:
            output = 'Mid'
        else:
            if years <= 10:
                output = 'Senior'
    return output

#------------------------------------------------------------------------------
def convert_to_lower(text):
    return text.lower()
#------------------------------------------------------------------------------

def remove_numbers(text):
    text = re.sub(r'\d+', '', text)
    return text

#------------------------------------------------------------------------------

def remove_http(text):
    text = re.sub("https?://t.co/[A-Za-z0-9]*", ' ', text)
    return text

#------------------------------------------------------------------------------

def remove_short_words(text):
    text = re.sub(r'bw{1,2}b', '', text)
    return text

#------------------------------------------------------------------------------

def remove_punctuation(text):
    punctuations = '''!()[]{};«№»:'",`./?@=#$-(%^)+&[*_]~'''
    no_punctuation = ""

    for char in text:
        if char not in punctuations:
            no_punctuation = no_punctuation + char

    return no_punctuation

#------------------------------------------------------------------------------

def remove_white_space(text):
    text = text.strip()
    return text

#------------------------------------------------------------------------------

def tokenizing(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)

    ## Remove Stopwords from tokens
    result = [i for i in tokens if not i in stop_words]
    return result

def preprocess_text(text):
# 1. Tokenise to alphabetic tokens
    text = remove_numbers(text)
    #text = remove_http(text)
    lemmatiser = WordNetLemmatizer()
    text = remove_punctuation(text)
    text = convert_to_lower(text)
    text = remove_white_space(text)
    #text = remove_short_words(text)
    tokens = tokenizing(text)

    # 2. POS tagging
    pos_map = {'J': 'a', 'N': 'n', 'R': 'r', 'V': 'v'}

    pos_tags_list = pos_tag(tokens)
    #print(pos_tags)
    # 3. Lowercase and lemmatise
    tokens = [lemmatiser.lemmatize(w.lower(), pos=pos_map.get(p[0], 'v')) for w, p in pos_tags_list]

    return tokens