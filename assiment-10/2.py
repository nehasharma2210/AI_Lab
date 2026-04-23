def goal_test(state):
    return state[1] == 'Clean' and state[2] == 'Clean'


def actions(state):
    return ['SUCK', 'LEFT', 'RIGHT']


def results(state, action):
    loc, A, B = state

    if action == 'SUCK':
        if loc == 'A':
            if A == 'Dirty':
                return [
                    ('A', 'Clean', B),
                    ('A', 'Clean', 'Clean')
                ]
            else:
                return [
                    ('A', 'Clean', B),
                    ('A', 'Dirty', B)
                ]

        if loc == 'B':
            if B == 'Dirty':
                return [
                    ('B', A, 'Clean'),
                    ('B', 'Clean', 'Clean')
                ]
            else:
                return [
                    ('B', A, 'Clean'),
                    ('B', A, 'Dirty')
                ]

    elif action == 'LEFT':
        return [('A', A, B)]

    elif action == 'RIGHT':
        return [('B', A, B)]


def AND_OR_SEARCH(state, visited, depth=0):
    print("  " * depth + "Checking State:", state)

    if goal_test(state):
        print("  " * depth + "Goal Reached")
        return True

    if state in visited:
        print("  " * depth + "Already Visited, skipping")
        return False

    visited.add(state)

    for action in actions(state):
        print("  " * depth + "Trying Action:", action)

        outcomes = results(state, action)

        success = True

        for result in outcomes:
            print("  " * depth + "Possible Outcome:", result)

            if not AND_OR_SEARCH(result, visited, depth + 1):
                success = False
                break

        if success:
            print("  " * depth + "Action works for all outcomes:", action)
            return True

    print("  " * depth + "Backtracking")
    return False


initial_state = ('A', 'Dirty', 'Dirty')

print("STARTING SEARCH\n")
result = AND_OR_SEARCH(initial_state, set())

print("\nFinal Result:", result)