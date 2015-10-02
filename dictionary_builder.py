import re
import os.path
from hash_table import HashTable

''' Module for generating a dictionary of words mapped to frequency aka histogram
from a list of tokens '''


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
                path = os.path.join(dirpath, name)
                build_histogram(path)

''' Opens a file and appends the contents into a list
    Creates a 'histogram' which is a dictionary of a word
    and frequency of the word in a file

    Returns a dictionary of words mapped to frequency
'''


def build_histogram_with_file(filename):
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


''' Builds a histogram '''


def build_histogram(tokens):
    histogram = HashTable()
    for token in tokens:
        if not histogram.contains(token):
            histogram[token] = 0
        histogram[token] += 1

    return histogram


def main(filename):
    # searchDir('/')
    build_histogram(filename)

if __name__ == '__main__':
    main('Resources/TestFiles/sherlock_holmes.txt')
