from adjective import *
from adverb import *
from article import *
from name import *
from noun import *
from verb import *


class Sentence:

    def basicSentence(self):
        #   article1, noun1, verb, article1, noun1
        #   noun has 50% chance of getting adj

        noun1    = Noun().random()
        article1 = Article(noun1.kind['plurality'])
        verb     = Verb(noun1.kind['plurality'])
        noun2    = Noun().random()
        article2 = Article(noun2.kind['plurality'])

        return article1, noun1, verb, article2, noun2


sentence = Sentence()
sentence = sentence.basicSentence()
string = ''

for word in sentence:
    string += word.value + ' '

print string
