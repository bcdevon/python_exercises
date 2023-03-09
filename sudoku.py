"""This module is used to check seduko games."""

example_seduko_board = [
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],

    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],

    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,8,9],
]


def is_row_valid(row_idx, seduko_board):
    """Given a row index and game board, return true if it is valid.

    The game board will be a list of lists. Each index (entry) will be a row of integers.
    The row should have all the numbers, 1 through 9, in any order. 

    Args:
        game_board:
            List of lists of numbers 1 through 9.

    Return:
        Return true if if the row is valid. 
        Example:

        row_idx = 0
        game_board = 
        [
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],

            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],

            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
        ]
        result = True

        row_idx = 0
        game_board = 
        [
            [1,1,1,1,-1,0,1,1,22],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],

            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],

            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
        ]
        result = False
    """
    sudoku_set = {1,2,3,4,5,6,7,8,9}
    get_set = set()
    for num in seduko_board[row_idx]:
        get_set.add(num)
    if sudoku_set == get_set:
        return True
    else:
        return False

is_row_valid(2, example_seduko_board)

def is_col_valid(col_idx, seduko_board):
    sudoku_set = {1,2,3,4,5,6,7,8,9}
    get_set = set()
    for num in seduko_board[row_idx, col_idx]


def is_board_valid(seduko_board):
    """Given a game board, return true if it is valid.

    The game board will be a list of lists. Each index (entry) will be a row of integers.
    Each row should have all the numbers, 1 through 9, in any order. 
    Each column should have all the numbers, 1 through 9, in any order. 

    Args:
        game_board:
            List of lists of numbers 1 through 9.

    Return:
        Return true if if the row is valid. 
        Example:

        game_board = 
        [
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],

            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],

            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
            [1,2,3,4,5,6,7,8,9],
        ]
        result = False

        game_board = 
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [2, 3, 4, 5, 6, 7, 8, 9, 1]
        ]
        result = True
    """
    row_indx = 0
    while row_indx < 9 and is_row_valid(row_indx, example_seduko_board) == True:
        row_indx += 1
        return True 
    else:
        return False
        
is_board_valid(example_seduko_board)

def sudoku_solver(game_board):
    """Given a game board, solve it.

    The game board will be a list of lists. Each index (entry) will be a row of integers.
    Each row should have all the numbers, 1 through 9, in any order. 
    Each column should have all the numbers, 1 through 9, in any order. 
    Any blanks will be noted with 0s.

    Args:
        game_board:
            List of lists of numbers 1 through 9.

    Example:
        game_board = 
        [
            [1, 0, 3, 0, 5, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 7, 0],
            [8, 9, 1, 0, 0, 4, 0, 6, 0],
            [0, 0, 9, 0, 2, 0, 0, 5, 0],
            [0, 7, 0, 9, 1, 0, 0, 0, 0],
            [0, 0, 7, 0, 9, 0, 0, 3, 0],
            [0, 0, 0, 0, 8, 0, 0, 2, 0],
            [0, 0, 0, 6, 0, 0, 0, 1, 2],
            [0, 0, 0, 0, 0, 0, 0, 9, 0]
        ]

    would become...

        game_board = 
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 1, 2, 3, 4, 5, 6, 7, 8],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [2, 3, 4, 5, 6, 7, 8, 9, 1]
        ]
    """