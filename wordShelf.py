fileName = 'wordListBlizz'

class WordShelf(object):

    articles   = []
    adjectives = []
    adverbs    = []

    nouns      =        {
        'singular': [],
        'plural':   []  }

    names      =        {
        'special': [],
        'other':   []   }

    #   VERBS:
    #       [singular, plural]
    #       [first, second, third]
    #       [past, present, future]

    #   add plurality
    verbs =             {
        'singular': {},
        'plural':   {}  }

    #   add person to each plurality
    for plurality in verbs:

        verbs[plurality] =  {
            'first':  {},
            'second': {},
            'third':  {}    }

    #   add tense to each person
    for plurality in verbs:
        for person in verbs[plurality]:

            verbs[plurality][person] =  {
                'past':    [],
                'present': [],
                'future':  []           }

    #   argument should be the name of the file
    def __init__( self, fileName ):

        self.wordList = [line for line in open(fileName)]

        #   Put the words in the wordfile where they belong
        if not self.articles:
            self.articles = self.getArticles()
        if not self.adjectives:
            self.adjectives = self.getAdjectives()
        # self.addAdverbs()
        # self.addNouns()
        # self.addNames()
        if not self.verbs['singular']['first']['past']:
            self.verbs = self.getVerbs()

    def getArticles( self ):

        articles = []

        #   tuple to point where start and end of articles is at
        start, end =                                (
                self.wordList.index('ARTICLES\n'),
                self.wordList.index('END\n')    )

        #   assignment
        for words in self.wordList[ start+1: end ]:
            articles.append( words.strip().replace('_',' ') )

        return articles

    def getAdjectives( self ):

        adjectives = []

        #   tuple to point where start and end of articles is at
        start, end =                                (
                self.wordList.index('ADJECTIVES\n'),
                self.wordList.index('ADVERBS\n')    )

        #   assignment
        for words in self.wordList[ start+1: end ]:
            adjectives.append( words.strip().replace('_',' ') )

        return adjectives

    def addAdverbs( self ):

        #   tuple to point where start and end of articles is at
        start, end =                              (
                self.wordList.index('ADVERBS\n'),
                self.wordList.index('NOUNS\n')    )

        #   assignment
        for words in self.wordList[ start+1: end ]:
            self.adverbs.append( words.strip().replace('_',' ') )

    def addNouns( self ):

        #   tuple to point where start and end of articles is at
        start, end =                              (
                self.wordList.index('NOUNS\n'),
                self.wordList.index('VERBS\n')    )

        #   separate nouns into words on left and words on right
        left, right = [], []

        #   split words into list, then append to left/right
        for words in self.wordList[ start+2: end ]:
            words = words.split()
            left.append( words[0].replace('_',' ') )
            right.append( words[1].replace('_',' ') )

        #   left are singular nouns, right are plural nouns
        self.nouns['singular'] = left
        self.nouns['plural']   = right

    def addNames( self ):

        #   tuple to point where start and end of articles is at
        #   this'll be done twice for 'other' and 'special'
        start, end =                              (
                self.wordList.index('NAMES\n'),
                self.wordList.index('    OTHER\n')    )

        #   assignment
        for words in self.wordList[ start+1: end ]:
            self.names['special'].append( words.strip().replace('_',' ') )

        #   tuple to point where start and end of articles is at
        #   second time for 'other'
        start, end =                               (
                self.wordList.index('    OTHER\n'),
                self.wordList.index('ARTICLES\n')  )

        #   assignment
        for words in self.wordList[ start+1: end ]:
            self.names['other'].append( words.strip().replace('_',' ') )

    def getVerbs( self ):

        #   let's first condense our list. . .
        start, end =                              (
                self.wordList.index('VERBS\n'),
                self.wordList.index('NAMES\n')    )

        verbList = self.wordList[ start: end ]

        #   { plurality: index }
        IndPlu = {
                'SINGULAR': 0,
                'PLURAL':   0   }

        for i, value in enumerate(verbList):
            for key in IndPlu:
                if key in value:
                    IndPlu[key] = i

        #   let's condense our list for the singulars
        littleList = verbList[ IndPlu['SINGULAR']: IndPlu['PLURAL'] ]

        #   { person, index }
        IndPerson = {
                'FIRST':  0,
                'SECOND': 0,
                'THIRD':  0     }

        for i, value in enumerate(littleList):
            for key in IndPerson:
                if key in value:
                    IndPerson[key] = i

        verbs = self.verbs
        #   SINGULAR
        #   FIRST
        for lines in littleList[ IndPerson['FIRST']+2: IndPerson['SECOND'] ]:
            lines = lines.split()
            verbs['singular']['first']['past'].append( lines[0].replace('_',' ') )
            verbs['singular']['first']['present'].append( lines[1].replace('_',' ') )
            verbs['singular']['first']['future'].append( lines[2].replace('_',' ') )

        #   SECOND
        for lines in littleList[ IndPerson['SECOND']+2: IndPerson['THIRD'] ]:
            lines = lines.split()
            verbs['singular']['second']['past'].append( lines[0].replace('_',' ') )
            verbs['singular']['second']['present'].append( lines[1].replace('_',' ') )
            verbs['singular']['second']['future'].append( lines[2].replace('_',' ') )

        #   THIRD
        for lines in littleList[ IndPerson['THIRD']+2: IndPlu['PLURAL'] ]:
            lines = lines.split()
            verbs['singular']['third']['past'].append( lines[0].replace('_',' ') )
            verbs['singular']['third']['present'].append( lines[1].replace('_',' ') )
            verbs['singular']['third']['future'].append( lines[2].replace('_',' ') )

        #   PLURAL

        #   let's condense our list for the singulars
        littleList = verbList[ IndPlu['PLURAL']: len(verbList) ]

        #   { person, index }
        IndPerson = {
                'FIRST':  0,
                'SECOND': 0,
                'THIRD':  0     }

        for i, value in enumerate(littleList):
            for key in IndPerson:
                if key in value:
                    IndPerson[key] = i

        #   FIRST
        for lines in littleList[ IndPerson['FIRST']+2: IndPerson['SECOND'] ]:
            lines = lines.split()
            verbs['plural']['first']['past'].append( lines[0].replace('_',' ') )
            verbs['plural']['first']['present'].append( lines[1].replace('_',' ') )
            verbs['plural']['first']['future'].append( lines[2].replace('_',' ') )

        #   SECOND
        for lines in littleList[ IndPerson['SECOND']+2: IndPerson['THIRD'] ]:
            lines = lines.split()
            verbs['plural']['second']['past'].append( lines[0].replace('_',' ') )
            verbs['plural']['second']['present'].append( lines[1].replace('_',' ') )
            verbs['plural']['second']['future'].append( lines[2].replace('_',' ') )

        #   THIRD
        for lines in littleList[ IndPerson['THIRD']+2: IndPlu['PLURAL'] ]:
            lines = lines.split()
            verbs['plural']['third']['past'].append( lines[0].replace('_',' ') )
            verbs['plural']['third']['present'].append( lines[1].replace('_',' ') )
            verbs['plural']['third']['future'].append( lines[2].replace('_',' ') )

        return verbs

wordShelf = WordShelf( fileName )
