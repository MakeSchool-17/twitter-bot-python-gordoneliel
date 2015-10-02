''' tokenize.py
    Module for creating a list of tokens from a source text
'''
import re
from string import punctuation


def tokenize(corpus):
    tokens = remove_punctuation(corpus)
    tokens = split_line(tokens)
    return tokens


def remove_punctuation(corpus):
    no_punct = re.sub('[,.()|;?]', '', corpus)
    no_punct = re.sub('--', ' ', no_punct)
    no_punct = re.sub('\".+?\"', ' ', no_punct)
    return no_punct.strip()


def split_line(corpus):
    return re.split('\s+', corpus)

if __name__ == '__main__':
    import sys
    source = open(sys.argv[1]).read()
    tokens = tokenize(source)
    source.close()
    print(tokens)
