from collections import deque

grid = [
[0,0,0,0,0,6,0,0,0],
[0,5,9,0,0,0,0,0,8],
[2,0,0,0,0,8,0,0,0],
[0,4,5,0,0,0,0,0,0],
[0,0,3,0,0,0,0,0,0],
[0,0,6,0,0,3,0,5,0],
[0,0,0,0,0,7,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,5,0,0,0,2]
]

# Domains
domains = {}
for r in range(9):
    for c in range(9):
        if grid[r][c] == 0:
            domains[(r,c)] = set(range(1,10))
        else:
            domains[(r,c)] = {grid[r][c]}

# Neighbors
def get_neighbors(r, c):
    neighbors = set()

    for i in range(9):
        neighbors.add((r,i))
        neighbors.add((i,c))

    br, bc = (r//3)*3, (c//3)*3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            neighbors.add((i,j))

    neighbors.remove((r,c))
    return neighbors

# Queue
queue = []
for cell in domains:
    for n in get_neighbors(*cell):
        queue.append((cell, n))

# Revise
def revise(X, Y):
    revised = False
    removed_vals = []

    for x in set(domains[X]):
        if all(x == y for y in domains[Y]):
            domains[X].remove(x)
            removed_vals.append(x)
            revised = True

    return revised, removed_vals

# AC-3
def ac3():
    step = 1
    total_removed = 0

    while queue:
        Xi, Xj = queue.pop()

        print("\nSTEP", step)
        print("Checking", Xi, "->", Xj)
        step += 1

        before = set(domains[Xi])

        revised, removed_vals = revise(Xi, Xj)

        if revised:
            removed_count = len(removed_vals)
            total_removed += removed_count

            print("Removed values:", removed_vals)
            print("Updated Domain", Xi, "=", domains[Xi])

            if not domains[Xi]:
                print("Domain empty. Problem unsolvable.")
                return False, total_removed

            for Xk in get_neighbors(*Xi):
                if Xk != Xj:
                    print("Re-adding arc:", Xk, "->", Xi)
                    queue.append((Xk, Xi))

    print("\nAC-3 finished")
    return True, total_removed

# Run
result, removed = ac3()

print("\nFinal Result:", result)
print("Total Values Removed:", removed)

# Domain size grid
print("\nDomain Size Grid:")
for r in range(9):
    row = []
    for c in range(9):
        row.append(str(len(domains[(r,c)])))
    print(" ".join(row))