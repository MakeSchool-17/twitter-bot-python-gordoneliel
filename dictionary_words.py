import random

'''/usr/share/dict/words'''

''' Opens a file and appends the contents into a list'''


def openfile(filename):
    word_list = []
    with open(filename, 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            word_list.append(a_line.rstrip())
    return word_list

''' Randomly picks a word from the list of words'''


def randomWord(word_list):

    random_index = random.randint(0, len(word_list) - 1)
    return word_list[randomIndex]


def main(filename):
    word_list = openfile(filename)
    word = randomWord(word_list)
    # print(word)

main('/usr/share/dict/words')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
