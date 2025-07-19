class GameState:
    def __init__(self, dimension):
        self.board = self.initialize_board(dimension)
        self.moveLog = []
        self.dimension = dimension
        self.computerToPlay = False
        self.BlackPlayerStacks = 0
        self.WhitePlayerStacks = 0
        self.BlackToPlayFirst = True #Za kasnije ako se odlucimo da napravimo da moze da se bira koja boja igra prva
        self.BlackPlayerToPlay = True
        self.AvailableMoves=[]
        self.PossibleGameStates = []
        self.CurrentPlayerColor=''

    def initialize_board(self, dimension):
        board = []

        empty_row = ['-'] * dimension
        empty_row2 = ['-'] * dimension
        board.append(empty_row)

        for i in range(1, dimension - 1):
            red = []
            if i % 2 != 0:
                for j in range(dimension):
                    if j % 2 == 0:
                        red.append('-')
                    else:
                        red.append('b')
            else:
                for j in range(dimension):
                    if j % 2 == 0:
                        red.append('w')
                    else:
                        red.append('-')

            board.append(red)
        board.append(empty_row2)

        return board