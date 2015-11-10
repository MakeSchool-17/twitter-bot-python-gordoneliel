''' tokenize.py
    Module for creating a list of tokens from a source text
'''
import re


def tokenize_source(corpus_raw):
    tokens = []
    start_words = []
    with open(corpus_raw, 'r') as a_file: # [brian] Nice! This is the best way to open a file.
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
    
    # [brian] I don't think the above `close()` works. For this to work you'd need to say:
    source = open(sys.argv[1])
    tokens = tokenize(source.read())
    source.close()

    # [brian] But even better is:
    with open(sys.argv[1]) as source:
        tokens = tokenize(source.read())

    print(tokens)
