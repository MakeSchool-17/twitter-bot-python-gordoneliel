import random
import dictionary_builder

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


def main(filename):
    # dictionary_builder.searchDir('/')
    histogram_list = dictionary_builder.build_histogram(filename)
    freq = frequency("mystery", histogram_list)
    words = unique_words(histogram_list)
    rand_word = random_word(histogram_list)
    print(freq)
    print(words)
    # print(histogram_list)
    print("Random word is: " + rand_word)
    # word = randomWord(histogram_list)
    # print(histogram_list)

# main('Resources/TestFiles/test_file.txt')
# main('Resources/TestFiles/robinson_crusoe.txt')
main('Resources/TestFiles/sherlock_holmes.txt')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
