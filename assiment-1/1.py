# -------- GRAPH DEFINITION (from given map) --------
graph = {
    "Syracuse": [("Buffalo", 150), ("New York", 254), ("Boston", 312)],

    "Buffalo": [("Cleveland", 189), ("Detroit", 256)],
    "New York": [("Philadelphia", 97), ("Pittsburgh", 305)],
    "Boston": [("Providence", 50), ("Portland", 107)],

    "Cleveland": [("Chicago", 345)],
    "Detroit": [("Chicago", 283)]
}

# -------- INITIALIZATION --------
start = "Syracuse"
goal = "Chicago"

# Each element: (node, cumulative_cost)
current_level = [(start, 0)]

level = 0

print("Level-wise sibling cumulative cost:\n")

# -------- LEVEL-WISE TRAVERSAL --------
while current_level:
    print(f"Level {level} nodes:", current_level)

    next_level = []

    for parent, parent_cost in current_level:
        if parent not in graph:
            continue

        children = graph[parent]

        # ----- sibling edge cost sum -----
        sibling_sum = 0
        for child, cost in children:
            sibling_sum += cost

        # ----- new cumulative cost -----
        new_cost = parent_cost + sibling_sum

        # ----- assign same cost to all siblings -----
        for child, _ in children:
            next_level.append((child, new_cost))

    # Stop if Chicago reached at this level
    for node, cost in next_level:
        if node == goal:
            print(f"\nReached {goal} at Level {level + 1}")
            print("Final Cost =", cost)
            exit()

    current_level = next_level
    level += 1
