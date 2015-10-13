import div_bot
import tokenize
import dictionary_builder
import sample
import sentence
from flask import Flask

''' Fetches a corpus for tokenizing '''
URLS_FILE = 'urls_file.txt'
app = Flask(__name__)


def fetch_corpus():
    return div_bot.main(URLS_FILE)


# @app.route('/')
def generate_sentence(tokens):
    return sentence.generate_sentence(tokens)


@app.route('/')
def main():
    # fetch_corpus()  # Fetch corpus and save to corpus.txt
    (start_words, tokens) = tokenize.tokenize_source("corpus.txt")
    # print("New worddd: ")
    # print(start_words)
    # print(tokens)
    # histogram = dictionary_builder.build_histogram(tokens)
    # random_word = sample_word(tokens)
    # print(random_word)
    # generate_sentence(tokens)
    print(str(generate_sentence(tokens)))

if __name__ == '__main__':
    main()
    # app.run()
