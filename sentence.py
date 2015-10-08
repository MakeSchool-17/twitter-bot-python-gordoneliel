''' sentence.py
    Module for generating sentences using markov chains
'''
import markov_model
import random
MAX_TOKENS = 20


def generate_sentence(tokens):
    markov_model_data = markov_model.MarkovModel(tokens).generate_markov_model()
    keys = start_keys(markov_model_data)
    start_word = random_word(keys)
    print("Start Word: " + start_word)

    sentence = ""
    token_count = 0
    # while token_count < MAX_TOKENS:
    #     #  Perform a random walk on the Markov Chain
    #     pass
    return keys

''' Picks a random word from the Markov chain '''


def random_word(word_list):
    random_index = random.randint(0, len(word_list) - 1)
    return word_list[random_index]


''' Fetches a list of keys from the Markov Model '''


def start_keys(markov_model_data):
    keys = list(markov_model_data.keys())
    return keys


def main():
    pass

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
