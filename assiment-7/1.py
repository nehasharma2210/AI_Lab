import random

N = 8
MAX_STEPS = 100

# Heuristic: attacking pairs
def heuristic(board):
    h = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

# Print board
def print_board(board):
    print("Board:", board)

# Generate random board
def random_board():
    return [random.randint(0, N - 1) for _ in range(N)]

# Steepest-Ascent Hill Climbing
def steepest(board):
    current = board[:]
    initial_h = heuristic(current)
    h = initial_h
    steps = 0

    print_board(current)
    print("Initial h =", h)

    while steps < MAX_STEPS:
        best_h = h
        next_state = current[:]

        # Explore all neighbors
        for col in range(N):
            original = current[col]

            for row in range(N):
                if row == original:
                    continue

                current[col] = row
                temp_h = heuristic(current)

                if temp_h < best_h:
                    best_h = temp_h
                    next_state = current[:]

            current[col] = original

        print(f"Step {steps+1}:")
        print_board(next_state)
        print("h =", best_h)

        # Local Minimum
        if best_h >= h:
            print("Local Minimum Reached (No better neighbor)\n")
            return initial_h, h, steps, "Fail"

        current = next_state
        h = best_h
        steps += 1

        if h == 0:
            print("Solution Found\n")
            return initial_h, h, steps, "Solved"

    return initial_h, h, steps, "Fail"


# MAIN
def main():
    success = 0

    print("\n===== FINAL TABLE =====")
    print("Trial | InitialH | FinalH | Steps | Status")

    for trial in range(1, 51):
        print("\n===========================")
        print(f"Trial {trial}")

        board = random_board()

        initial_h, final_h, steps, status = steepest(board)

        print(f"Final h = {final_h}")
        print(f"Steps = {steps}")
        print(f"Status = {status}")

        # Table row
        print(f"{trial} | {initial_h} | {final_h} | {steps} | {status}")

        if status == "Solved":
            success += 1

    print("\nTotal Success =", success, "/ 50")


if __name__ == "__main__":
    main()