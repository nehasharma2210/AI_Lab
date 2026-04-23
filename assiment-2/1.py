import copy

GOAL = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

start_state = [
    [1,0,2],
    [3,4,5],
    [6,7,8]
]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

moves = [(0,1),(0,-1),(1,0),(-1,0)]

reached = set()
reached.add(tuple(map(tuple, start_state)))

queue = [(start_state, 0)]   # (state, level)
state_count = 1

while queue:
    current_state, level = queue.pop(0)

    if current_state == GOAL:
        print(f"Goal reached at level {level}, states explored {state_count}")
        break

    row, col = find_zero(current_state)

    for dx, dy in moves:
        new_r = row + dx
        new_c = col + dy

        if 0 <= new_r < 3 and 0 <= new_c < 3:
            temp = copy.deepcopy(current_state)

            # swap
            temp[row][col], temp[new_r][new_c] = temp[new_r][new_c], temp[row][col]

            state_tuple = tuple(map(tuple, temp))

            if state_tuple not in reached:
                reached.add(state_tuple)
                state_count += 1
                queue.append((temp, level+1))


count = [0,100]
reached=set()
reached.add(tuple(map(tuple,start_state)))
def DFS(state,reached,count):
    if(state==GOAL):
        print(f"Goal is found with total state count = {count[0]}")
        return True

    if(count[1]<0):
        return False
    row,col=find_zero(state)
    for dx,dy in moves:
        newx=dx+row
        newy=dy+col
        if 0<=newx<3 and 0<=newy< 3:
            tem=copy.deepcopy(state)
            tem[row][col],tem[newx][newy]=tem[newx][newy], tem[row][col]
            state_tuple = tuple(map(tuple, tem))
            if state_tuple not in reached:
                reached.add(state_tuple)
                count[0]+= 1
                count[1]-=1
                if DFS(tem,reached,count):
                    return True
    return False


if not DFS(start_state, reached, count):
    print("Goal not reachable")