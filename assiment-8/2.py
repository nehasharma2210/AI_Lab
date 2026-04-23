import random

# DATA
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

# COST FUNCTION (VERY IMPORTANT)
def cost(route):
    total = 0
    for i in range(len(route)-1):
        total += dist[route[i]][route[i+1]]
    total += dist[route[-1]][route[0]]  # return to start
    return total


# RANDOM ROUTE
def random_route():
    r = list(range(8))
    random.shuffle(r)
    return r


# SELECTION (BEST 2)
def selection(pop):
    pop.sort(key=lambda x: cost(x))
    print("\n>> Selected Parents:")
    for p in pop[:2]:
        print([cities[x] for x in p], "Cost =", cost(p))
    return pop[:2]


# ONE-POINT CROSSOVER
def crossover_one(p1, p2):
    point = random.randint(1, 6)
    print(f"One-point crossover at index {point}")

    child = p1[:point] + [x for x in p2 if x not in p1[:point]]
    return child


# TWO-POINT CROSSOVER
def crossover_two(p1, p2):
    a, b = sorted(random.sample(range(8), 2))
    print(f"Two-point crossover between {a} and {b}")

    child = [-1]*8
    child[a:b] = p1[a:b]

    fill = [x for x in p2 if x not in child]
    j = 0
    for i in range(8):
        if child[i] == -1:
            child[i] = fill[j]
            j += 1
    return child


# MUTATION (SWAP)
def mutate(route):
    i, j = random.sample(range(8), 2)
    route[i], route[j] = route[j], route[i]
    print(f"Mutation: swapped index {i} and {j}")
    return route


# GENETIC ALGORITHM
def genetic(crossover_type="one", generations=10, pop_size=6):
    print(f"\n===== GA using {crossover_type}-point crossover =====")

    # initial population
    pop = [random_route() for _ in range(pop_size)]

    for gen in range(generations):
        print(f"\n--- Generation {gen+1} ---")

        for p in pop:
            print([cities[x] for x in p], "Cost =", cost(p))

        parents = selection(pop)

        new_pop = parents[:]

        while len(new_pop) < pop_size:
            if crossover_type == "one":
                child = crossover_one(parents[0], parents[1])
            else:
                child = crossover_two(parents[0], parents[1])

            print("Child before mutation:", [cities[x] for x in child])

            child = mutate(child)

            print("Child after mutation:", [cities[x] for x in child], "Cost =", cost(child))

            new_pop.append(child)

        pop = new_pop

    best = min(pop, key=lambda x: cost(x))
    print("\n FINAL BEST PATH:", [cities[x] for x in best], "Cost =", cost(best))


# RUN BOTH
genetic("one")
genetic("two")