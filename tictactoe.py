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
    
    # Start counter for number of moves already made
    num_X = 0
    num_O = 0

    # Check each cell to count moves of each player
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_X += 1
            elif board[i][j] == O:
                num_O += 1

    # Determine next player who has the next turn.
    if num_X > num_O:
        return O  
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Initialize set to collect all empty cells 
    moves = set()

    # Add all empty cells to set
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i,j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create deepcopy of existing board
    new = copy.deepcopy(board)

    # Make move on new board after checking whose turn it is
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
    # Crate list containing both players to loop through. 
    player = (X,O)

    # Create variable to indicate who is winning
    winner = None

    # CHeck if one player has three in a row
    for a in player:
        # Diagonals
        if board[0][0] == a and board[1][1] == a and board[2][2] == a:
            winner = a
        elif board[2][0] == a and board[1][1] == a and board[0][2] == a:
            winner = a
        # Horizontals
        elif board[0][0] == a and board[0][1] == a and board[0][2] == a:
            winner = a
        elif board[1][0] == a and board[1][1] == a and board[1][2] == a:
            winner = a
        elif board[2][0] == a and board[2][1] == a and board[2][2] == a:
            winner = a
        # Verticals
        elif board[0][0] == a and board[1][0] == a and board[2][0] == a:
            winner = a
        elif board[0][1] == a and board[1][1] == a and board[2][1] == a:
            winner = a
        elif board[0][2] == a and board[1][2] == a and board[2][2] == a:
            winner = a
        
    return winner


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
