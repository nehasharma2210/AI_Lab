import math

# Tic-Tac-Toe Board
board = [' ' for _ in range(9)]

# Print board
def print_board(b):
    print("\n")
    print(b[0], "|", b[1], "|", b[2])
    print("--+---+--")
    print(b[3], "|", b[4], "|", b[5])
    print("--+---+--")
    print(b[6], "|", b[7], "|", b[8])
    print("\n")

# Check winner
def check_winner(b):
    win_states = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for state in win_states:
        if b[state[0]] == b[state[1]] == b[state[2]] != ' ':
            return b[state[0]]
    if ' ' not in b:
        return 'Tie'
    return None

# Minimax with printing
node_count = 0

def minimax(b, depth, is_max):
    global node_count
    node_count += 1

    winner = check_winner(b)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif winner == 'Tie':
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                print("MAX exploring move at index", i, "depth", depth)
                val = minimax(b, depth+1, False)
                b[i] = ' '
                best = max(best, val)
        print("MAX depth", depth, "returns", best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                print("MIN exploring move at index", i, "depth", depth)
                val = minimax(b, depth+1, True)
                b[i] = ' '
                best = min(best, val)
        print("MIN depth", depth, "returns", best)
        return best

# Find best move
def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            print("Move", i, "has value", move_val)

            if move_val > best_val:
                best_val = move_val
                move = i

    return move

# Run
print("Initial Board")
print_board(board)

move = best_move()
print("Best Move is:", move)

print("Total nodes explored:", node_count)