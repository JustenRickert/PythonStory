import random
from wordShelf import WordShelf

arguments =         [
        'singular',
        'plural'    ]

class Noun( WordShelf ):

    def __str__( self ):
        return self.value

    def __init__( self, *arg ):
        super( Noun, self ).__init__()

        self.kind =             {
                'plurality': '' }

        if arg:
            arg = arg[0]

        if (arg) and (arg not in arguments):
            raise ValueError("arg is bad")
        if arg:
            self.value = self.random( arg )
        else:
            self.value = self.random()

        self.kind =             {
                'plurality': '' }

    def random( self, *arg ):

        if arg:
            arg = arg[0]

        if arg:
            value = random.choice( self.nouns[arg] )
            self.kind['plurality'] = arg
        else:
            plurality = random.choice( arguments )
            value = random.choice( self.nouns[plurality] )
            self.kind['plurality'] = plurality

        return value

    def nextRandom( self ):
        self.nouns[self.kind].remove( self.value )

        if not self.nouns:
            raise RuntimeError("no nouns left")

        self.__init__()

        return self

noun2 = Noun('singular')
noun = Noun('plural')
print noun, noun2
