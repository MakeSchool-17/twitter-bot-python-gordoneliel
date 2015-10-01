''' tokenize.py
    Module for creating a list of tokens from a source text
'''
import re


def tokenize(corpus):
    tokens = remove_punctuation(corpus)
    tokens = split_line(tokens)
    return tokens


def remove_punctuation(corpus):
    no_punct = re.sub('[,.()]', '', corpus)
    no_punct = re.sub('--', ' ', no_punct)
    no_punct = re.sub(r'".*?"', no_punct)
    return no_punct


def split_line(corpus):
    return re.split('\s+', corpus)
