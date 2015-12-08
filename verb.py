import random
from wordShelf import WordShelf

fileName = 'wordListBlizz'

''' Specific verbs are callable as object member variables
    eg: Verb( 'singular', 'first', 'past' ) returns members like

    Verb.plurality returns 'singular' or 'plural'

    if no args are given, then random members will be assigned. '''

arguments = {
        'plurality': ['singular', 'plural'],
        'person':    ['first', 'second', 'third'],
        'tense':     ['past', 'present', 'future']  }

class Verb( WordShelf ):

    def __str__( self ):
        return self.value

    ''' Expected arguments are: Verb( * Plurality, Person, Tense )  '''
    ''' If no args found for each any arg, a random assignment is
            called for each.                                        '''
    def __init__( self, *args ):
        super( Verb, self ).__init__( fileName )

        #   The word
        self.value = ''

        #   [plurality, person, tense]
        self.kind = {
                'plurality': '',
                'person':    '',
                'tense':     ''     }

        #   calls dispatch for each arg
        for arg in args:
            for possible in arguments:
                if arg in arguments[possible]:
                    self.kind[possible] = self.dispatch( arg )

        #   create random for plurity, person, tense if not given as arg
        for key in self.kind:
            if self.kind[key] == '':
                if key == 'plurality':
                    self.kind[key] = self.getPlurality()
                elif key == 'person':
                    self.kind[key] = self.getPerson()
                elif key == 'tense':
                    self.kind[key] = self.getTense()

        self.value = self.random()

    def random( self ):
        verb = random.choice(
                self.verbs[ self.kind['plurality'] ]
                          [ self.kind['person'] ]
                          [ self.kind['tense'] ]     )
        return verb

    ''' member functions '''
    def nextRandom( self ):

        #   delete current verb so it can't be got again
        #   verbs[][][].remove( self.value )
        self.verbs[ self.kind['plurality'] ]\
                  [ self.kind['person'] ]\
                  [ self.kind['tense'] ].remove(self.value)

        #   re-run init to recreate verb
        self.__init__(
               self.kind['plurality'],
               self.kind['person'],
               self.kind['tense']      )

        return self

    ''' HELPER FUNCTIONS '''
    def dispatch( self, arg ):

        #   if I want the argument called, then I call it by a dictionary
        #   dispatch [ 'singular', 'first', 'future' ] calls
        #      addTense( 'singular' ), addPerson( 'first' ), et c.
        return {
            'singular': self.getPlurality('singular'),
            'plural':   self.getPlurality('plural'),

            'first':    self.getPerson('first'),
            'second':   self.getPerson('second'),
            'third':    self.getPerson('third'),

            'past':     self.getTense('past'),
            'present':  self.getTense('present'),
            'future':   self.getTense('future')
        }[arg]

    #   methods
    def getPlurality( self, *plurality ):

        #   if given an argument, then match with plurality
        if plurality:
            plurality = plurality[0]

        #   otherwise give a random plurality
        else:
            plurality = [
                    'singular',
                    'plural',   ]
            plurality = random.choice( plurality )

        return plurality


    def getPerson( self, *person ):

        if person:
            person = person[0]

        else:
            person = [
                    'first',
                    'second',
                    'third',    ]
            person = random.choice( person )

        return person

    def getTense( self, *tense ):

        if tense:
            tense = tense[0]

        else:
            tense = [
                    'past',
                    'present',
                    'future'    ]
            tense = random.choice( tense )

        return tense

verb = Verb()
print( verb.nextRandom );
