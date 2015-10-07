''' sentence.py
    Module for generating sentences using markov chains
'''
import markov_model


def generate_sentence(tokens):
    markov_model.MarkovModel(tokens).generate_markov_model()


def main():
    pass

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
