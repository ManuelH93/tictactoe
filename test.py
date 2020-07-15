from tictactoe import terminal, actions, result, utility, player

X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, X, O],
         [O, X, EMPTY],
         [X, EMPTY, O]]

def maxvalue(board):
    """
    MAXVALUE picks action in ACTIONS(board) that produces highest value of MINVALUE(RESULT(board, action))
    """

    if terminal(board) == True:
        return(utility(board))
    
    v = float("-inf")
    for a in actions(board):
        v = max(v, minvalue(result(board, a)))
    return(v)

def minvalue(board):
    """
    MINVALUE picks action in ACTIONS(board) that produces lowest value of MAXVALUE(RESULT(board, action))
    """
   
    if terminal(board) == True:
        return(utility(board))
    
    v = float("inf")
    for a in actions(board):
        v = min(v, maxvalue(result(board, a)))
    return(v)

print(terminal(board))
print(player(board))
print(maxvalue(board))
print(minvalue(board))