#from tictactoe import player,result

X = "X"
O = "O"
EMPTY = None

state = [[O, EMPTY, X],
         [EMPTY, O, X],
         [O, X, X]]

horizontal_X = [0,0,0]
horizontal_O = [0,0,0]
vertical_X = [0,0,0]
vertical_O = [0,0,0]

for i in range(3):
    for j in range(3):
        if state[i][j] == X:
            horizontal_X[i] += 1
            vertical_X[j] += 1
        if state[i][j] == O:
            horizontal_O[i] += 1
            vertical_O[j] += 1

diagonal_X = [0,0]
diagonal_O = [0,0]

if state[0][0] == X and state[1][1] == X and state[2][2] == X:
    diagonal_X[0] == 3
if state[2][0] == X and state[1][1] == X and state[0][2] == X:
    diagonal_X[1] == 3

if state[0][0] == O and state[1][1] == O and state[2][2] == O:
    diagonal_O[0] += 3
if state[2][0] == O and state[1][1] == O and state[0][2] == O:
    diagonal_O[1] += 3

all_X = horizontal_X + vertical_X + diagonal_X
all_O = horizontal_O + vertical_O + diagonal_O

if max(all_X) == 3:
    print(X)

if max(all_O) == 3:
    print(O)

#for each x in horizontal vertical diagonal:
#    if max(x) = 3

#X_entries = [horizontal_X, vertical_X, diagonal_X]
#print(X_entries)
#max_Xvalues = list(min(s) for s in zip(*X_entries))
#print(max_Xvalues)