from tictactoe import result

X = "X"
O = "O"
EMPTY = None

state = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, O, EMPTY],
         [EMPTY, X, EMPTY]]

position = (0,0)

result(state, position)

#print(state)
#print(state[1][1])