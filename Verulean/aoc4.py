import numpy as np
from aoc_util import aoc_input


class Bingo(object):
    """
    A class that represents a collection of bingo boards that all progress from
    the same drawn numbers. On initialization, determines the order in which 
    the boards will finish and sorts the boards from the first bingo to the last.
    
    Contains a method to compute the bingo score for any given board in the sorted
    collection.
    
    Parameters
    ----------
    data : list[str]
        A list containing the input data for the game. data[0] is a comma-separated
        string containing the order in which numbers are drawn during the game,
        and all subsequent elements of data are string representations of 5x5
        bingo boards.
        
        Note: Equivalent to the raw input split by '\\n\\n'.
    
    Attributes
    ----------
    __draw_order : np.ndarray
        A 1D integer array that contains the order of numbers drawn during the
        bingo game.
    __N : int
        The number of bingo boards stored.
    __boards : np.ndarray
        A 3D integer array of shape (__N, 5, 5) containing the original bingo
        boards. Indexing is of the form (board, row, column).
    __marked : np.ndarray
        A 3D boolean array of the same shape as __boards that represents which
        entries in __boards have been drawn and marked.
    __bingo_index : np.ndarray
        A 1D integer array of length __N that contains the indices of
        __draw_order that the game must be played to for each board to have a
        bingo.
    """
    def __init__(self, data):
        """Initialize self."""
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
        """
        Returns a vector representing when each board achieves a bingo.
        
        Parameters
        ----------
        self : Bingo
        
        Returns
        -------
        ind : np.ndarray
            A 1D integer array. For the ith board in __boards, ind[i]
            gives the index in __draw_order that must be drawn to for
            the ith board to have gotten a bingo.
            """
        row, col = [np.any(np.all(self.__marked, axis=a), axis=1) for a in (1, 2)]
        return row | col
    
    def draw(self):
        """
        Populates __bingo_index with the first index of __draw_order 
        for which every board in __boards gets a bingo.
        """
        for i, n in enumerate(self.__draw_order):
            pre = self.bingos()
            self.__marked[self.__boards == n] = True
            post = self.bingos()
            self.__bingo_index[pre ^ post] = i
    
    def sort(self):
        """Sorts all boards and their associated arrays by the values in 
        __bingo_index, in ascending order."""
        ind = np.argsort(self.__bingo_index)
        for arr in (self.__boards, self.__marked, self.__bingo_index):
            arr[:] = arr[ind]
    
    def score(self, i):
        """Returns the score of the ith board in __boards just after it gets
        a bingo.
        
        Parameters
        ----------
        self : Bingo
        i : int
            Index of the scored board.
        
        Returns
        -------
        score : int
            The score of the ith board. Its value is the sum of all unmarked
            entries on the board, multiplied by the last number drawn to 
            complete its bingo.
        """
        board = self.__boards[i]
        b = self.__bingo_index[i]
        n = self.__draw_order[b]
        score = n * np.sum(board[~np.isin(board, self.__draw_order[:b+1])])
        return score


def solve():
    data = aoc_input(4, sep='\n\n')
    squid_game = Bingo(data)
    return squid_game.score(0), squid_game.score(-1)