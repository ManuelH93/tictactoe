"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_X = 0
    num_O = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_X += 1
            elif board[i][j] == O:
                num_O += 1

    if num_X > num_O:
        print(O)
        return O  
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    moves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new = copy.deepcopy(board)

    for i, x in enumerate(new):
        for j, a in enumerate(x):
            if (i,j) == action and a != EMPTY:
                raise Exception("selected cell is already taken")
            elif (i,j) == action and player(board) == X:
                new[i][j] = X
            elif (i,j) == action and player(board) == O:
                new[i][j] = O

    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
