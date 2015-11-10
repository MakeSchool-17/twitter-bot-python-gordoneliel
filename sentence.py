''' sentence.py
    Module for generating sentences using markov chains
'''
import markov_model
import random
MAX_TOKENS = 20


def generate_sentence(tokens):
    markov_model_data = markov_model.MarkovModel(tokens).generate_markov_model()
    word_list = list(markov_model_data.keys())
    start_word = random_word(word_list)
    cap_word = start_word.capitalize()
    # print("Start Word: " + start_word)

    sentence = ""
    sentence += cap_word
    while True:
        #  Perform a random walk on the Markov Chain
        next_word_list = markov_model_data[start_word]
        next_word = random_word_dict(next_word_list)
        sentence += " " + next_word
        if next_word[-1] == '.':
            break

        start_word = next_word
    return sentence

    # [brian] You could write the above:

    words = []
    word = start_word
    while not word.endswith('.'):
        next_word_list = markov_model_data[word]
        word = random_word_dict(next_word_list)
        words.append(word)
    return ' '.join(words)

    # it's a little faster and slightly more pythonic, we try to avoid while True loops
    # as much as we can. In most languages string concatenation isn't super quick, it's
    # faster to combine all your words into one sentence all at once.

''' Picks a random word from the Markov chain '''


def random_word(word_list):
    random_index = random.randint(0, len(word_list) - 1)
    return word_list[random_index]

    # [brian] You can write the above as:

    return random.choice(word_list)


def random_word_dict(histogram_list):
    random_index = random.randint(0, len(histogram_list) - 1)
    histogram = list(histogram_list.keys())
    return histogram[random_index]

    # [brian] This isn't a ton cleaner, but you could also say (assuming you're
    # using py3):

    return histogram_list[random.choice(list(histogram_list.keys()))]

    # If you're using py2:

    return histogram_list[random.choice(histogram_list.keys())]

    # This one will work on both, but it's even harder to read unless you've
    # used the random module a lot:

    return random.sample(histogram_list.items(), 1)[0][1]

''' Fetches a list of keys from the Markov Model '''


def start_keys(markov_model_data):
    keys = list(markov_model_data.keys())
    return keys


def main():
    pass

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
