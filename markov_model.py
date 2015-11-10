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
                    markov_table[previous_token] = inner_markov_table # [brian] This line is unnecessary
                    # When you read from `markov_table` you're not
                    # making a copy of the dict which is already there, you're
                    # getting a variable which points to the exact same dict
                    # which is in the dictionary, when you modify it you're
                    # also modifying the one in `markov_table`, so you don't
                    # need to put it back into `markov_table`.
                else:
                    #  If the word exists in our dict, increase the occurance
                    #  Increment count of current_token
                    inner_markov_table = markov_table[previous_token]
                    inner_markov_table[current_token] += 1
                    markov_table[previous_token] = inner_markov_table
            previous_token = current_token

        # print(markov_table)
        return markov_table

# [brian] Instead of the above, you could write this:

from collections import defaultdict
def generate_markov_model(self):
    markov_table = {}
    previous_token = "."
    for current_token in self.tokens:
        inner_table = markov_table.setdefault(previous_token, defaultdict(int))
        inner_table[current_token] += 1
        previous_token = current_token
    return markov_table

# the pattern you used above of "if this key doesn't exist use a default value, if the key does
# exist do something to id" is super common. So python has added two different ways of writing it,
# both of which are shown above.

# `dictionary.setdefault('key', 10)` will return the key at 'key' if it exists. If it doesn't exist
# it will first call `dictionary['key'] = 10` and then return 10.

# defaultdicts let you act as if you're dealing with a regular dict and just call `dictionary['key']`,
# but behind the scenes they do the same thing. Both are super useful ways of making your code shorter
# and easier to write.

if __name__ == '__main__':
    import sys
    MarkovModel().generate_word_frequency(sys.argv[1])
