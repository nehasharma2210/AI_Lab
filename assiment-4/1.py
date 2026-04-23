cities = [
    "Syracuse",     # 0
    "Buffalo",      # 1
    "New York",     # 2
    "Philadelphia", # 3
    "Cleveland",    # 4
    "Pittsburgh",   # 5
    "Detroit",      # 6
    "Chicago"       # 7
]

# Graph as adjacency list (using indexes)
graph = [
    [1, 2, 3],      # Syracuse
    [0, 6],         # Buffalo
    [0, 3],         # New York
    [0, 2, 5],      # Philadelphia
    [6, 7],         # Cleveland
    [3, 4],         # Pittsburgh
    [1, 4, 7],      # Detroit
    []              # Chicago
]

# helper values (estimated distance to Chicago)
helper = [
    650,  # Syracuse
    540,  # Buffalo
    790,  # New York
    760,  # Philadelphia
    350,  # Cleveland
    460,  # Pittsburgh
    280,  # Detroit
    0     # Chicago
]

def best_first_search(start, goal):
    frontier = [start]
    reached = []
    parent = [-1] * len(cities)

    while len(frontier) > 0:

        # select node with minimum value
        current = frontier[0]
        for node in frontier:
            if helper[node] < helper[current]:
                current = node

        frontier.remove(current)
        reached.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in reached and neighbor not in frontier:
                parent[neighbor] = current
                frontier.append(neighbor)

    # path reconstruction
    path = list()
    node = goal
    while node != -1:
        path.append(cities[node])
        node = parent[node]
    path.reverse()

    print("Path Found:")
    for city in path:
        print(city)

    print("\nCities Explored:")
    for i in  reached:
        print(cities[i])

    print("\nNumber of Cities Traveled:", len( reached))


# Start = Syracuse (0), Goal = Chicago (5)
best_first_search(0, 5)
