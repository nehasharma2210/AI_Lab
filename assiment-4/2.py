# 0 = free path, 1 = wall, S = entry, G = exit

floor = [
    ['S', 0, 1, 0, 0],
    [0,  0, 1, 0, 1],
    [1,  0, 0, 0, 0],
    [1,  1, 0, 1, 0],
    [0,  0, 0, 0, 'G']
]

rows = len(floor)
cols = len(floor[0])

# Find begin and goal
for i in range(rows):
    for j in range(cols):
        if floor[i][j] == 'S':
            begin = (i, j)
        if floor[i][j] == 'G':
            goal = (i, j)

# Manhattan distance  
def helper(block):
    return abs(block[0] - goal[0]) + abs(block[1] - goal[1])

def best_first_search():
    frontier = [begin]
    reached = []
    parent = {}

    while frontier:
        # choose block with minimum helper
        current = frontier[0]
        for block in frontier:
            if helper(block) < helper(current):
                current = block

        frontier.remove(current)
        reached.append(current)

        if current == goal:
            break

        row, col = current
        moves = [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]

        for new_row, new_col in moves:
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if floor[new_row][new_col] != 1 and (new_row,new_col) not in reached and (new_row,new_col) not in frontier:
                    parent[(new_row,new_col)] = current
                    frontier.append((new_row,new_col))

    # Reconstruct path
    path = []
    node = goal
    while node != begin:
        path.append(node)
        node = parent[node]
    path.append(begin)
    path.reverse()

    print("Evacuation Path:")
    for step in path:
        print(step)

    print("\nTotal blocks Explored:", len(reached))

best_first_search()
