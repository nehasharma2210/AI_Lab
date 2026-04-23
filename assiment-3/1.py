import random
rooms={
    'A':"DIRT",
    'B':"DIRT",
    'C':"DIRT"
}
current_location='A'
rules=[['A',['DIRT','SUCK'],['CLEAN','LEFT']],
['B',['DIRT','SUCK'],['CLEAN',random.choice(['LEFT','RIGHT'])]],
['C',['DIRT','SUCK'],['CLEAN','RIGHT']]]

move=[['A','B'],['B',['A','C']],['C','B']]
map={
    'A':0,
    'B':1,
    'C':2,
    'CLEAN':1,
    'DIRT':2
}
for i in range(10):
    status=rooms[current_location]
    precept=(current_location,status)
    action=rules[map[current_location]][map[status]][1]
    print(f"{precept}\t{action}", end="")
    if action=='SUCK':
        rooms[current_location]="CLEAN"
        print(f"\t\t\t{current_location}")
    else :
        idx = map[current_location]
        if idx == 1:  
            current_location = random.choice(move[1][1])
        else:
            current_location = move[idx][1]
        print(f"\t\t\t{current_location}")
