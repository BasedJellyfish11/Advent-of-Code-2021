import numpy as np


fmt_dict = {'sep': '\n\n'}

class Bingo(object):
    def __init__(self, data):
        draws, boards = data[0], data[1:]
        
        self.__draw_order  = np.array(draws.split(sep=','), dtype=int)
        
        self.__N           = len(boards)
        self.__boards      = np.zeros((self.__N, 5, 5), dtype=int)
        self.__marked      = np.zeros_like(self.__boards, dtype=bool)
        self.__bingo_index = np.zeros(self.__N, dtype=int)
        
        # Populate __boards
        for b, board in enumerate(boards):
            for r, row in enumerate(board.split(sep='\n')):
                self.__boards[b,r] = row.split()
        
        # Compute bingo indices and sort by bingo order
        self.draw()
        self.sort()
    
    def bingos(self):
        row, col = [np.any(np.all(self.__marked, axis=a), axis=1) for a in (1, 2)]
        return row | col
    
    def draw(self):
        for i, n in enumerate(self.__draw_order):
            pre = self.bingos()
            self.__marked[self.__boards == n] = True
            post = self.bingos()
            self.__bingo_index[pre ^ post] = i
    
    def sort(self):
        ind = np.argsort(self.__bingo_index)
        for arr in (self.__boards, self.__marked, self.__bingo_index):
            arr[:] = arr[ind]
    
    def score(self, i):
        board = self.__boards[i]
        b = self.__bingo_index[i]
        n = self.__draw_order[b]
        unmarked_sum = np.sum(board, where=~np.isin(board, self.__draw_order[:b+1]))
        return n * unmarked_sum

def solve(data):
    squid_game = Bingo(data)
    return squid_game.score(0), squid_game.score(-1)