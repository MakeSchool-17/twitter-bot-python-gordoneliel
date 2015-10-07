import div_bot
import tokenize
import dictionary_builder
import sample
import sentence

''' Fetches a corpus for tokenizing '''
URLS_FILE = 'urls_file.txt'


def fetch_corpus():
    return div_bot.main(URLS_FILE)


def tokenize_source(corpus_raw):
    tokens = []
    with open(corpus_raw, 'r') as a_file:
        for a_line in a_file:
            words = tokenize.tokenize(a_line)
            tokens += words
    return tokens


def sample_word(tokens):
    return sample.random_weighted_word(tokens)


def generate_sentence(tokens):
    return sentence.generate_sentence(tokens)


def main():
    # fetch_corpus()  # Fetch corpus and save to corpus.txt
    tokens = tokenize_source("corpus.txt")
    # print(tokens)
    # histogram = dictionary_builder.build_histogram(tokens)
    random_word = sample_word(tokens)
    print(random_word)
    generate_sentence(tokens)


if __name__ == '__main__':
    main()
