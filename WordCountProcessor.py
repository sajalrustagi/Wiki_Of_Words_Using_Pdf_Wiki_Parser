# Takes a fileName, parses the file whether pdf/wiki, convert it to keywords and return
# the count of words

import FileContentParser
import TextProcessorAndTokenizer
from collections import Counter


def get_word_count(filename):
    # get the text content present in file
    text = FileContentParser.parse(filename)
    # get the keywords from the text
    keywords = TextProcessorAndTokenizer.get_keywords(text)
    # return the count of words in the file
    return Counter(keywords)
