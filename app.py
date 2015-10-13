import div_bot
import tokenize
import dictionary_builder
import sample
import sentence
from flask import Flask
import os

PORT = int(os.environ.get('PORT', 5000))
DEBUG_MODE = False

''' Fetches a corpus for tokenizing '''
URLS_FILE = 'urls_file.txt'
app = Flask(__name__)

my_tokens = []


def fetch_corpus():
    return div_bot.main(URLS_FILE)


# @app.route('/')
def generate_sentence(tokens):
    return sentence.generate_sentence(tokens)


@app.route('/')
def main():
    # fetch_corpus()  # Fetch corpus and save to corpus.txt
    # (start_words, tokens) = tokenize.tokenize_source("corpus.txt")
    # print("New worddd: ")
    # print(start_words)
    # print(tokens)
    # histogram = dictionary_builder.build_histogram(tokens)
    # random_word = sample_word(tokens)
    # print(random_word)
    # generate_sentence(tokens)
    return (str(generate_sentence(tokens)))

if __name__ == '__main__':
    (start_words, tokens) = tokenize.tokenize_source("corpus.txt")
    my_tokens = tokens
    app.run(debug=DEBUG_MODE, port=PORT)
