import math

board = [' ' for _ in range(9)]
node_count_ab = 0

def print_board(b):
    print("\n")
    print(b[0], "|", b[1], "|", b[2])
    print("--+---+--")
    print(b[3], "|", b[4], "|", b[5])
    print("--+---+--")
    print(b[6], "|", b[7], "|", b[8])
    print("\n")

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

def minimax_ab(b, depth, alpha, beta, is_max):
    global node_count_ab
    node_count_ab += 1

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
                print("MAX exploring", i, "depth", depth, "alpha", alpha, "beta", beta)
                val = minimax_ab(b, depth+1, alpha, beta, False)
                b[i] = ' '
                best = max(best, val)
                alpha = max(alpha, best)

                if beta <= alpha:
                    print("PRUNING at MAX node index", i)
                    break

        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                print("MIN exploring", i, "depth", depth, "alpha", alpha, "beta", beta)
                val = minimax_ab(b, depth+1, alpha, beta, True)
                b[i] = ' '
                best = min(best, val)
                beta = min(beta, best)

                if beta <= alpha:
                    print("PRUNING at MIN node index", i)
                    break

        return best

def best_move_ab():
    best_val = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            val = minimax_ab(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            print("Move", i, "value", val)

            if val > best_val:
                best_val = val
                move = i

    return move

# Run
print("Initial Board")
print_board(board)

move = best_move_ab()
print("Best Move using Alpha-Beta:", move)

print("Total nodes explored with Alpha-Beta:", node_count_ab)