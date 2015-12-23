import random
from wordShelf import WordShelf

arguments = [
        'singular',
        'plural']


class Noun(WordShelf):

    def __str__(self):
        return self.value

    def __init__(self, *arg):
        super(Noun, self).__init__()

        self.kind = {
                'plurality': ''}

        if arg:
            arg = arg[0]

        if (arg) and (arg not in arguments):
            raise ValueError("arg is bad")
        if arg:
            self.random(arg)
        else:
            self.random()

    def random(self, *arg):

        if arg:
            arg = arg[0]

        if arg:
            value = random.choice(self.nouns[arg])
            self.kind['plurality'] = arg
        else:
            plurality = random.choice(arguments)
            value = random.choice(self.nouns[plurality])
            self.kind['plurality'] = plurality

        self.value = value
        return self

    def nextRandom(self):
        self.nouns[self.kind['plurality']].remove(self.value)

        if not (self.nouns):
            raise RuntimeError("no nouns left")

        return self.random()

    def plurality(self):
        return self.kind['plurality']



noun = Noun()
print noun.kind
