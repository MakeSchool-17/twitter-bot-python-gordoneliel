import re
import os.path
from hash_table import *


'''
    Crawls a directory for a list of .txt files and builds a dictionary of
    words mapped to frequency of the words
'''


# The top argument for walk.
topdir = '.'

# The arg argument for walk, and subsequently ext for step
exten = '.txt'


def searchDir(root_dir):
    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            if name.lower().endswith(exten):
                print(os.path.join(dirpath, name))
                build_histogram(name)

''' Opens a file and appends the contents into a list
    Creates a 'histogram' which is a dictionary of a word
    and frequency of the word in a file

    Returns a dictionary of words mapped to frequency
'''


def tokenize_line(a_line):
    tokens = remove_punctuation(a_line)
    tokens = split_line(tokens)
    return tokens


def remove_punctuation(a_line):
    no_punct = re.sub('[,.()]', '', a_line)
    no_punct = re.sub('--', ' ', no_punct)
    no_punct = re.sub(r'".*?"', no_punct)
    return no_punct


def split_line(a_line):
    return re.split('\s+', a_line)


def build_histogram(filename):
    word_dict = HashTable()
    list_word = []
    with open(filename, 'r') as a_file:
        for a_line in a_file:
            words = re.findall(r"[a-zA-Z]+", a_line)
            for word in words:
                list_word.append(word)
                if not word_dict.contains(word):
                    word_dict[word] = 0
                word_dict[word] += 1
    return word_dict, list_word


def build_histogramPy(filename):
    word_dict = {}
    with open(filename, 'r') as a_file:
        for a_line in a_file:
            words = re.findall("[a-zA-Z]+", a_line.lower())
            for word in words:
                if word not in word_dict:
                    word_dict[word] = 0
                word_dict[word] += 1
    return word_dict
if __name__ == '__main__':
    main()
