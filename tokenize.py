''' tokenize.py
    Module for creating a list of tokens from a source text
'''
import re


def tokenize_source(corpus_raw):
    tokens = []
    start_words = []
    with open(corpus_raw, 'r') as a_file:
        for a_line in a_file:
            words = tokenize(a_line)
            start_words.append(words[0])
            tokens += words
    return (start_words, tokens)


def tokenize(corpus):
    tokens = remove_punctuation(corpus)
    tokens = split_line(tokens)
    return tokens


def remove_punctuation(corpus):
    no_punct = re.sub('[,()|;]', '', corpus)
    no_punct = re.sub('--', ' ', no_punct)
    return no_punct.strip()


def split_line(corpus):
    return re.split('\s+', corpus)

if __name__ == '__main__':
    import sys
    source = open(sys.argv[1]).read()
    tokens = tokenize(source)
    source.close()
    print(tokens)
