import random
from wordShelf import WordShelf

class Adjective( WordShelf ):

    def __str__( self ):
        return self.value

    def __init__( self ):
        super( Adjective, self ).__init__()
        self.value = self.random()

    def random( self ):
        return random.choice( self.adjectives )

    def nextRandom( self ):
        self.adjectives.remove( self.value )

        if not len(self.adjectives):
            raise RuntimeError("no adjectives left")

        return self.random()

adjective = Adjective()
