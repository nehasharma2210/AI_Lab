import random
import itertools

# Distance matrix
cities = ['A','B','C','D','E','F','G','H']
dist = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

# Cost function
def cost(route):
    total = 0
    for i in range(len(route)-1):
        total += dist[route[i]][route[i+1]]
    total += dist[route[-1]][route[0]]  # return to start
    return total

# Generate neighbors (swap)
def neighbors(route):
    neigh = []
    for i in range(len(route)):
        for j in range(i+1, len(route)):
            new = route[:]
            new[i], new[j] = new[j], new[i]
            neigh.append(new)
    return neigh

# Local Beam Search
def beam_search(k, max_iter=10):
    print(f"\n===== Beam Width k = {k} =====")

    # initial random states
    states = []
    for _ in range(k):
        r = list(range(8))
        random.shuffle(r)
        states.append(r)

    for step in range(max_iter):
        print(f"\n--- Iteration {step+1} ---")

        all_neighbors = []
        for s in states:
            neigh = neighbors(s)
            all_neighbors.extend(neigh)

        # sort by cost
        all_neighbors.sort(key=lambda x: cost(x))

        # pick best k
        states = all_neighbors[:k]

        for i, s in enumerate(states):
            print(f"State {i+1}: {[cities[x] for x in s]} Cost = {cost(s)}")

    best = states[0]
    print("\nFINAL BEST PATH:", [cities[x] for x in best], "Cost =", cost(best))

# Run for k = 3,5,10
beam_search(3)
beam_search(5)
beam_search(10)