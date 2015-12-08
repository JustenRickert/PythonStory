import random
from wordShelf import WordShelf

fileName = 'wordListBlizz'

class Article( WordShelf ):

    def __str__( self ):
        return self.value

    def __init__( self, *args ):
        super( Article, self ).__init__( fileName )

        print self.articles

        possibleArgs = [
                'single',
                'plural'    ]

article = Article()

