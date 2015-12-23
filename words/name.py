import random
from wordShelf import WordShelf

arguments =         [
        'special',
        'other'     ]

class Name( WordShelf ):

    def __str__( self ):
        return self.value

    def __init__( self, *arg ):
        super( Name, self ).__init__()

        #   self.kind?
        self.kind = ''

        #   undoes the tuple
        if arg:
            arg = arg[0]

        if (arg) and (arg not in arguments):
            raise ValueError("bad arg")

        if arg:
            self.value = self.random( arg )
        else:
            self.value = self.random()

    def random( self, *arg ):

        specialOrOther = random.choice( arguments )

        if arg:
            arg = arg[0]
            name = random.choice( self.names[arg] )
            self.kind = arg
        else:
            name = random.choice( self.names[specialOrOther] )
            self.kind = specialOrOther

        return name

    def nextRandom( self ):
        self.names[self.kind].remove( self.value )

        if not self.names:
            raise RuntimeError("no names left")

        return self.random( self.kind )


name = Name('special')
