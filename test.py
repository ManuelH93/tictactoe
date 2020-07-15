from tictactoe import maxvalue, minvalue, actions, utility, result, player, terminal

X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

print(player(board))

if terminal(board) == True:
    print(None)
elif player(board) == X:
    options = []
    utility = []
    for a in actions(board):
        options.append((a, minvalue(result(board, a))))
        utility.append(minvalue(result(board, a)))
    
    
    for action, value in options:
        if value == max(utility):
            print(action)
elif player(board) == O:
    options = []
    utility = []
    for a in actions(board):
        options.append((a, maxvalue(result(board, a))))
        utility.append(maxvalue(result(board, a)))
    for action, value in options:
        if value == min(utility):
            print(action)