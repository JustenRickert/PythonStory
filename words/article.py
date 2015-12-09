import random
from wordShelf import WordShelf

arguments =         {
        'singular',
        'plural'    }

class Article( WordShelf ):

    def __str__( self ):
        return self.value

    def __init__( self, *arg ):
        super( Article, self ).__init__()

        self.kind =             {
                'plurality': '' }

        if arg:
            self.value = self.random( arg )
        else:
            self.value = self.random( arg )

    #   NOTE: articles are NOT removed
    def random( self, *arg ):
        if (arg) and (arg in arguments):

            singleArgs = ['a', 'the']

            #   if singular
            if arg in singularArgs:
                while arg not in singularArgs:
                    self.value = self.random()
                    self.kind['plurality'] = 'singular'

            #   plural
            else:
                while arg in singularArgs:
                    self.value = self.random()
                    self.kind['plurality'] = 'plural'

        return self.value

    #   nextRandom doesn't really make sense for articles I don't think.
    #   Possibly TODO
    def nextRandom( self ):
        raise RuntimeError("no Article.nextRandom function")


article = Article()

