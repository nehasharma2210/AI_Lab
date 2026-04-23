import random
import math

N = 8
MAX_STEPS = 100

# Heuristic
def heuristic(board):
    h = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def print_board(board):
    print("Board:", board)

def random_board():
    return [random.randint(0, N - 1) for _ in range(N)]

#  FIRST CHOICE
def first_choice(board):
    current = board[:]
    initial_h = heuristic(current)
    h = initial_h
    steps = 0

    print_board(current)
    print("Initial h =", h)

    while steps < MAX_STEPS:
        improved = False

        for col in range(N):
            original = current[col]

            for row in range(N):
                if row == original:
                    continue

                current[col] = row
                temp_h = heuristic(current)

                if temp_h < h:
                    h = temp_h
                    improved = True
                    break

            if improved:
                break
            current[col] = original

        print(f"Step {steps+1}:")
        print_board(current)
        print("h =", h)

        if not improved:
            print("Local Minimum Reached\n")
            return initial_h, h, steps, "Fail"

        steps += 1

        if h == 0:
            print("Solution Found\n")
            return initial_h, h, steps, "Solved"

    return initial_h, h, steps, "Fail"


#  STEEPEST (used in random restart)
def steepest(board):
    current = board[:]
    h = heuristic(current)

    for _ in range(MAX_STEPS):
        best_h = h
        next_state = current[:]

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

        if best_h >= h:
            return False

        current = next_state
        h = best_h

        if h == 0:
            return True

    return False


#  RANDOM RESTART
def random_restart():
    steps = 0
    for restart in range(50):
        board = random_board()
        print(f"Restart {restart+1}:", board)

        if steepest(board):
            print("Solution Found via Restart\n")
            return 0, 0, steps, "Solved"

    print("Failed after multiple restarts\n")
    return 0, 0, steps, "Fail"


#  SIMULATED ANNEALING
def simulated_annealing(board):
    current = board[:]
    initial_h = heuristic(current)
    h = initial_h
    T = 100.0
    steps = 0

    print_board(current)
    print("Initial h =", h)

    while steps < MAX_STEPS:
        next_state = current[:]

        col = random.randint(0, N - 1)
        next_state[col] = random.randint(0, N - 1)

        new_h = heuristic(next_state)

        if new_h < h:
            current = next_state
            h = new_h
        else:
            prob = math.exp((h - new_h) / T)
            if random.random() < prob:
                current = next_state
                h = new_h

        print(f"Step {steps+1}:")
        print_board(current)
        print("h =", h)

        if h == 0:
            print("Solution Found\n")
            return initial_h, h, steps, "Solved"

        T *= 0.95
        steps += 1

    print("Failed\n")
    return initial_h, h, steps, "Fail"


#  MAIN
def main():
    s1 = s2 = s3 = 0

    print("\n===== FINAL COMPARISON TABLE =====")
    print("Trial | FC | RR | SA")

    for trial in range(1, 51):
        print("\n===========================")
        print("Trial", trial)

        board = random_board()

        print("\n--- First Choice ---")
        _, _, _, status1 = first_choice(board)

        print("\n--- Random Restart ---")
        _, _, _, status2 = random_restart()

        print("\n--- Simulated Annealing ---")
        _, _, _, status3 = simulated_annealing(board)

        print(f"{trial} | {status1} | {status2} | {status3}")

        if status1 == "Solved": s1 += 1
        if status2 == "Solved": s2 += 1
        if status3 == "Solved": s3 += 1

    print("\n===== FINAL RESULT =====")
    print("First Choice:", s1, "/50")
    print("Random Restart:", s2, "/50")
    print("Simulated Annealing:", s3, "/50")


if __name__ == "__main__":
    main()