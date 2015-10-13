from hash_table import HashTable
import dictionary_builder


class MarkovModel:
    def __init__(self, tokens=None):
        self.tokens = tokens
        self.markov_chain = {}
        self.word_frequency = self.generate_word_frequency()

    def generate_word_frequency(self):
        return dictionary_builder.build_histogram(self.tokens)

    ''' Generates a markov model from 'tokens' '''

    def generate_markov_model(self):
        markov_table = {}
        previous_token = "."
        # inner_markov_table = {}
        for current_token in self.tokens:
            # If its a new word add to dictionary
            if previous_token not in markov_table:
                markov_table[previous_token] = {current_token: 1}
                inner_markov_table = markov_table[previous_token]
            else:
                if current_token not in markov_table[previous_token]:
                    inner_markov_table = markov_table[previous_token]
                    inner_markov_table[current_token] = 1
                    markov_table[previous_token] = inner_markov_table
                else:
                    #  If the word exists in our dict, increase the occurance
                    #  Increment count of current_token
                    inner_markov_table = markov_table[previous_token]
                    inner_markov_table[current_token] += 1
                    markov_table[previous_token] = inner_markov_table
            previous_token = current_token

        # print(markov_table)
        return markov_table

if __name__ == '__main__':
    import sys
    MarkovModel().generate_word_frequency(sys.argv[1])
