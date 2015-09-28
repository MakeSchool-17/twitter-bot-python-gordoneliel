''' Maps a word to frequency and weight in sample text'''


class Word_Frequency_Map(object):
    def __init__(self, word):
        super(Word_Frequency_Map, self).__init__()
        self.word = word
        self.wordMap = {}

    def addWordMap(self, word, frequency):
        if word not in word_dict:
            word_dict[word] = 0
        word_dict[word] += 1
