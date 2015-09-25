import random
import os.path
import re

'''/usr/share/dict/words'''
'''Resources/TestFiles/diary_of_a_turk.txt'''
''' Searches a directory for files to parse to histogram'''


# def searchDir(root_dir):
#     for root, subFolders, files in os.walk(root_dir):
#         for file in files:


''' Opens a file and appends the contents into a list
    Creates a 'histogram' which is a dictionary of a word
    and frequency of the word in a file

'''


def histogram(filename):
    word_dict = {}
    with open(filename, 'r') as a_file:
        for a_line in a_file:
            words = re.split('\W+', a_line)
            for word in words:
                if word not in word_dict:
                    word_dict[word] = 0
                word_dict[word] += 1
    return word_dict

''' Returns the number of unique words in the histogram '''


def unique_words(histogram):
    return len(histogram)

''' Returns the frequency of a word in a histogram
    histogram - The histogram to get word and frequency
'''


def frequency(word, histogram):
    return histogram[word]

''' Randomly picks a word from the list of words'''


def randomWord(histogram_list):
    random_index = random.randint(0, len(histogram_list) - 1)
    return histogram_list[random_index]


def main(filename):
    # searchDir('/')
    histogram_list = histogram(filename)
    freq = frequency("mystery", histogram_list)
    words = unique_words(histogram_list)
    print(freq)
    print(words)
    # word = randomWord(histogram_list)
    # print(histogram_list)

# main('Resources/TestFiles/test_file.txt')
# main('Resources/TestFiles/robinson_crusoe.txt')
main('Resources/TestFiles/sherlock_holmes.txt')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
