import random
from wordShelf import *

class Adverb( WordShelf ):

    def __str__( self ):
        return self.value

    def __init__( self ):
        super( Adverb, self ).__init__()
        self.value = self.random()

    def random( self ):
        return random.choice( self.adverbs )

    def nextRandom( self ):
        self.adverbs.remove( self.value )

        if not self.adverbs:
            raise RuntimeError("no adverbs left")

        return self.random()


adverb = Adverb()
