''' Maps a word to frequency and weight in sample text'''

# [brian] It's usually a bad idea to do this:
from hash_table import *
# later when you call `HashTable()` isn't not obvious where it came from.  I
# mean, in _this_ file it's pretty obvious, but for a larger program with lots
# of classes it's really useful to be able to search for `HashTable`, find the
# result at the top of the file, and then jump to that file.

class Word_Frequency_Map(object):
    def __init__(self, word):
        super(Word_Frequency_Map, self).__init__()
        self.word = word
        self.word_map = HashTable()

    def addWordMap(self, word, frequency):
        if word not in word_map:
            word_dict[word] = 0
        word_dict[word] += 1
