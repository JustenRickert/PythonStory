import random
from wordShelf import WordShelf

arguments = [
        'singular',
        'plural']


class Article(WordShelf):

    def __str__(self):
        return self.value

    def __init__(self, *arg):
        super(Article, self).__init__()

        self.kind = {
                'plurality': ''}

        if arg:
            self.value = self.random(arg)
        else:
            self.value = self.random()

    def random(self, *arg):
        if (arg) and (type(arg) is tuple):
            arg = arg[0]

        #   NOTE: articles are NOT removed
        if (arg) and (arg in arguments):

            singleArgs = ['a', 'the']

            #   if singular
            if arg is 'singular':
                while self.value not in singleArgs:
                    self.value = self.random()
                    self.kind['plurality'] = 'singular'

            #   plural
            else:
                while self.value is 'a':
                    self.value = self.random()
                    self.kind['plurality'] = 'plural'
        else:
            self.value = random.choice(self.articles)

        return self.value

    def nextRandom(self):
        #   nextRandom doesn't really make sense for articles I don't think.
        #   Possibly TODO
        raise RuntimeError("no Article.nextRandom function")


article = Article()
