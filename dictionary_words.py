import random
from dictionary_builder import *
import timeit

'''/usr/share/dict/words'''
'''Resources/TestFiles/diary_of_a_turk.txt'''


''' Returns the number of unique words in the histogram '''


def unique_words(histogram):
    return len(histogram)

''' Returns the frequency of a word in a histogram
    histogram - The histogram to get word and frequency
'''


def frequency(word, histogram):
    return histogram[word]

''' Randomly picks a word from the list of words'''


def random_word(histogram_list):
    random_index = random.randint(0, len(histogram_list) - 1)
    histogram = list(histogram_list.keys())
    return histogram[random_index]

''' Computes the weight of a word in a corpus '''


def compute_word_weight(histogram):
    frequency_histogram = HashTable()
    for word in histogram.keys():
        if word is None:
            print(word)
        word_frequency = frequency(word, histogram) / unique_words(histogram)
        frequency_histogram[word] = word_frequency
    return frequency_histogram

''' A Naive implementation of random word with weight '''


def random_weighted_word(word_list):
    random_index = random.randint(0, len(word_list) - 1)
    return word_list[random_index]


def main(filename):

    histogram_list, word_list = build_histogram(filename)

    randWeight = random_weighted_word(word_list)
    print("Weight Random: " + str(randWeight))

    freq = frequency("mystery", histogram_list)
    freq_project = frequency("works", histogram_list)
    # print(frequency(wl[-2], histogram_list))
    words = unique_words(histogram_list)
    rand_word = random_word(histogram_list)

    print(freq)
    print("Freq of works: " + str(freq_project))
    print(words)
    #
    print("Random word is: " + rand_word)
    # print("Word Weights: \n")
    # print(compute_word_weight(histogram_list))


# main('Resources/TestFiles/test_file.txt')
# main('Resources/TestFiles/robinson_crusoe.txt')


if __name__ == "__main__":
    main('Resources/TestFiles/sherlock_holmes.txt')
