# This is the main file that initializes a wiki of words and demo how wiki works

from collections import Counter
import WordCountProcessor

files_already_in_wiki = ['input/Bill_Gates.pdf',
                         'https://en.wikipedia.org/wiki/Steve_Jobs',
                         'https://en.wikipedia.org/wiki/Jeff_Bezos']
new_file_to_add = 'input/Mark_Zuckerberg.pdf'


class WikiOfWords:

    def __init__(self):
        self.wiki_of_words = Counter([])

    def add_words_to_counter(self, counter):
        self.wiki_of_words += counter

    def get_top_100(self):
        return [word for word, word_count in self.wiki_of_words.most_common(100)]

    def add_file(self, filename):
        print "Words count for file ", filename, " : ", WordCountProcessor.get_word_count(filename)
        self.add_words_to_counter(WordCountProcessor.get_word_count(filename))

# initialises wiki of words
wiki_of_words = WikiOfWords()

# get all the files from initial list and populate the wiki
for filename in files_already_in_wiki:
    wiki_of_words.add_file(filename)

# get top 100 words in initial list
wiki_of_words_initial = wiki_of_words.get_top_100()

# adds new file 'Mark_Zuckerberg.pdf' to the wiki
wiki_of_words.add_file(new_file_to_add)
# get top 100 words in updated wiki
wiki_of_words_with_new_file = wiki_of_words.get_top_100()

# computes the difference in both the wiki's before and after addition of new file
words_removed_after_new_file = set(wiki_of_words_initial) - set(wiki_of_words_with_new_file)
words_added_after_new_file = set(wiki_of_words_with_new_file) - set(wiki_of_words_initial)

print "After addition of new file"
print "words added to top 100 wiki : ", words_added_after_new_file
print "words removed from top 100 wiki : ", words_removed_after_new_file
