''' cleanup.py
    Module for cleaning up a source text fromt the web
'''
import requests


DIV_BOT_API_TOKEN = '4bcc1f46992cc569dc63ace7d25d6f8a'
DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'


def fetch_article(url):

    params = {'token': DIV_BOT_API_TOKEN,
              'url': url,
              'discussion': 'false'}

    res = requests.get(DIFFBOT_API_URL, params)
    res_obj = res.json()['objects'][0]

    return res_obj['text']


def main(args):
    urls_file = open(args)
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        url = line.strip()
        article = fetch_article(url)
        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
    output_file.close()


if __name__ == '__main__':
    import sys
    urls_file = sys.argv[1]
    main(urls_file)
