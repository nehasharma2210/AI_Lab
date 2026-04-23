graph = {
    "Raj": ["Priya", "Sunil"],
    "Priya": ["Raj", "Aarav", "Neha"],
    "Aarav": ["Priya", "Neha", "Arjun"],
    "Sunil": ["Raj", "Akash", "Sneha"],
    "Akash": ["Sunil", "Neha"],
    "Neha": ["Priya", "Akash", "Rahul"],
    "Sneha": ["Sunil", "Rahul", "Maya"],
    "Rahul": ["Neha", "Sneha", "Pooja"],
    "Maya": ["Sneha"],
    "Arjun": ["Aarav", "Pooja"],
    "Pooja": ["Rahul", "Arjun"]
}

start="Raj"
queue=[(start,0)]
level=0;
visited=set(start)
print("breadth-first search:\n")
while queue:
    print(f"level {len(queue)} nodes: {queue}")
    next_level=[]
    for parent in queue:
        if parent[0] not in graph:
            continue
        children=graph[parent[0]]
        for child in children:
            if  child not in visited:
                next_level.append((child,level+1))
                visited.add(child)
    queue=next_level
    level+=1

print("\nDepth-first search:\n")
stack=[start]
reached=set(start)
while(stack):
    print(f"exploring  node {stack[len(stack)-1]}")
    parent=stack.pop()
    if parent not in graph:
        continue
    children=graph[parent]
    for child in children:
        if child not in reached:
            stack.append(child)
            reached.add(child)