# simple reflex agent
data={
    'A': 'Dirty',
    'B': 'Dirty',
    'C': 'Clean'
}
location='A'
def reflex_agent(location, status):
    if status == 'Dirty':
        return 'Clean'
    else:
        if location == 'A':
            return 'MOVE_RIGHT'
        elif location == 'B':
            return 'MOVE_RIGHT'
        elif location == 'C':
            return 'MOVE_LEFT'

print("Percept\t\tAction\t\tLocation")

for step in range(6):
    status = data[location]
    percept = (location, status)

    action = reflex_agent(location, status)

    print(f"{percept}\t{action}\t\t{location}")

    # Perform action
    if action == 'Clean':
        data[location] = 'Clean'
    elif action == 'MOVE_RIGHT':
        if location == 'A':
            location = 'B'
        elif location == 'B':
            location = 'C'
    elif action == 'MOVE_LEFT':
        if location == 'C':
            location = 'B'
        elif location == 'B':
            location = 'A'