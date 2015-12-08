import random
from wordShelf import WordShelf

fileName = 'wordListBlizz'

class Adjective( WordShelf ):

    def __init__( self ):
        super( Adjective, self ).__init__( fileName )

        print len(self.adjectives)

adjective = Adjective()
