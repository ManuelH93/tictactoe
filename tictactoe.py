"""
Tic Tac Toe Player
"""
print('test')
import math, copy, random

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

    # Ceck if one player has three in a row
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
    # Create variable to indicate if game is over
    game_over = False

    # Check if there are still empty cells left
    empty_cells = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_cells += 1

    # Check if empty cells left or player has won
    if empty_cells == 0:
        game_over = True
    elif winner(board) == None:
        game_over = False
    else:
        game_over = True
    return game_over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Create variable to keep track of utility of game
    utility = 0

    # Check who won the game
    if winner(board) == X:
        utility = 1
    elif winner(board) == O:
        utility = -1
    else:
        utility = 0
    return utility


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    elif player(board) == X:
        return maxaction(board)
    elif player(board) == O:
        return minaction(board)


def maxvalue(board, alpha, beta):
    """
    MAXVALUE returns maximum utility that can result from picking action in ACTIONS(board).
    """
    # return utility if game finished
    if terminal(board) == True:
        return(utility(board))
    # find maxvalue through iterative process with minvalue function using pruning
    maxv = float("-inf")
    for a in actions(board):
        maxv = max(maxv, minvalue(result(board, a), alpha, beta))
        if maxv > beta:
            return maxv
        if maxv > alpha:
            alpha = maxv
    return maxv

def minvalue(board, alpha, beta):
    """
    MINVALUE returns minimum utility that can result from picking action in ACTIONS(board).
    """
    # return utility if game finished
    if terminal(board) == True:
        return(utility(board))
    # find maxvalue through iterative process with minvalue function using pruning
    minv = float("inf")
    for a in actions(board):
        minv = min(minv, maxvalue(result(board, a), alpha, beta))
        if minv < alpha:
            return minv
        if minv < beta:
            beta = minv
    return minv


def maxaction(board):
    """
    MAX picks action in ACTIONS(board) that produces highest value of MINVALUE(RESULT(board, action))
    """
    # for all possible actions, collect the minvalue of the resulting board
    options = []
    for a in actions(board):
        options.append((a, minvalue(result(board, a), float("-inf"), float("inf"))))
    # extract utility (minvalues)
    utility = []
    for a, b in options:
        utility.append(b)
   # select options with highest minvalue
    max_options = []
    for action, value in options:
        if value == max(utility):
            max_options.append(action)
    return(random.choice(max_options)) 


def minaction(board):
    """
    MIN picks action in ACTIONS(board) that produces smallest value of MAXVALUE(RESULT(board, action))
    """
    # for all possible actions, collect the maxvalue of the resulting board
    options = []
    for a in actions(board):
        options.append((a, maxvalue(result(board, a), float("-inf"), float("inf"))))
    # extract utility (maxvalues)
    utility = []
    for a, b in options:
        utility.append(b)
    # select options with lowest maxvalue
    min_options = []
    for action, value in options:
        if value == min(utility):
            min_options.append(action)
    return(random.choice(min_options)) 
