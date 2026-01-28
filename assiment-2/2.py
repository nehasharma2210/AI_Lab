# ----------- GOAL STATE -----------
GOAL = (0, 1, 2,
        3, 4, 5,
        6, 7, 8)

# ----------- POSSIBLE MOVES -----------
MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start):
    queue = []                 # queue as list
    queue.append((start, 0))   # (state, depth)

    visited = set()
    visited.add(start)

    explored = 0
    front = 0                  # pointer (instead of pop)

    while front < len(queue):
        state, depth = queue[front]
        front += 1
        explored += 1

        if state == GOAL:
            return explored, depth

        zero = state.index(0)

        for move in MOVES[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, depth + 1))

# ----------- START STATE -----------
start_state = (7, 2, 4,
               5, 0, 6,
               8, 3, 1)

states_explored, goal_depth = bfs(start_state)

print("States explored using BFS:", states_explored)
print("Depth of goal state:", goal_depth)
