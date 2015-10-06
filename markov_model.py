from hash_table import HashTable


class MarkovModel:
    def __init__(self, tokens=None):
        self.tokens = tokens
        self.markov_chain = markov_chain



    def generate_markov_model(self, arg):
        markov_table = HashTable()
        for token, next_token in zip(self.tokens):
            if token not in markov_table:
                markov_table[token] = next_token
            else:
                #  Increment count of token
