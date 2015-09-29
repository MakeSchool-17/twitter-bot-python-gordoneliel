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


def build_histogram(filename):
    word_dict = HashTable()
    with open(filename, 'r') as a_file:
        for a_line in a_file:
            words = re.split('\W+', a_line.lower())
            for word in words:
                if not word_dict.contains(word):
                    word_dict[word] = 0
                word_dict[word] += 1
    return word_dict

if __name__ == '__main__':
    main()
