# Converts text variable which contains all the text derived
# from our PDF/wiki file to keywords. Text likely contains a lot of spaces, possibly junk such as '\n' etc.
# These functions will clean our text variable, and return it as a list of keywords.

import unicodedata
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# we'll create a new list which contains punctuation we wish to clean
punctuations = ['(', ')', ';', ':', '[', ']', ',', '.']

# We initialize the stopwords variable which is a list of words like
# "The", "I", "and", etc. that don't hold much value as keywords
stop_words = stopwords.words('english')

def get_keywords(text):

    # remove non ascii characters
    text = gracefully_degrade_to_ascii(text)
    # remove non english characters
    text = remove_non_english_characters(text)
    # The word_tokenize() function will break our text phrases into # individual words
    tokens = word_tokenize(text)
    # convert to lower case
    lower_words = [word.lower() for word in tokens]
    # We create a list comprehension which only returns a list of words
    # that are NOT IN stop_words and NOT IN punctuations.
    keywords = [word for word in lower_words if word not in stop_words and word not in punctuations]
    return keywords


def gracefully_degrade_to_ascii(text):
    return unicodedata.normalize('NFKD',text).encode('ascii','ignore')


def remove_non_english_characters(text):
    return re.sub(r'[^a-zA-Z ]', '', text)


