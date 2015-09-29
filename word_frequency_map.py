''' Maps a word to frequency and weight in sample text'''
from hash_table import *

class Word_Frequency_Map(object):
    def __init__(self, word):
        super(Word_Frequency_Map, self).__init__()
        self.word = word
        self.word_map = HashTable()

    def addWordMap(self, word, frequency):
        if word not in word_map:
            word_dict[word] = 0
        word_dict[word] += 1
