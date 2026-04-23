city={"Syracuse": [("Buffalo", 150), ("New York", 254), ("Boston", 312)],

    "Buffalo": [("Cleveland", 189), ("Detroit", 256)],
    "New York": [("Philadelphia", 97), ("Pittsburgh", 305)],
    "Boston": [("Providence", 50), ("Portland", 107)],

    "Cleveland": [("Chicago", 345)],
    "Detroit": [("Chicago", 283)]}
start="Syracuse"
goal="Chicago"
level=0
queue=[ (start,level) ]
cost=0
while queue:
    print(f"level {len(queue)} nodes: {queue}")
    next_level=[]
    for parent in queue:
        if parent[0] not in city:
            continue
        children=city[parent[0]]
        for child in children:
                cost+=child[1]
                if child[0]==goal:
                    print(f"Reached { goal } at level {level}")
                    print(f"final cost {cost}")
                else :
                     next_level.append((child[0],level+1))
    queue=next_level
    level+=1


stack = [start]
cost=0
print("depth-first search:\n")

while stack:
    print(f" visiting :{stack[len(stack)-1]}")

    parent=stack.pop()
    
    if parent not in city:
            continue
    children = city[parent]


    for child, child_cost in city[parent]:
        print(f"Exploring: {parent} => {child} (cost={child_cost})")

        cost += child_cost   #  step cost

        if child == goal:
            print(f"\nReached {goal}")
            print(f"Final Search Effort Cost = {cost}")

        stack.append(child)
        
    