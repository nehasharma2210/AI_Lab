import copy
variables = ["P1","P2","P3","P4","P5","P6"]
domains = {v: {"R1","R2","R3"} for v in variables}
domains["P1"]={"R1"}
neighbors = {
    "P1": ["P2","P3","P6"],
    "P2": ["P1","P3","P4"],
    "P3": ["P1","P2","P5"],
    "P4": ["P2","P6"],
    "P5": ["P3","P6"],
    "P6": ["P1","P4","P5"]
}

def revise(X, Y):
    revised = False
    print(f"\nChecking Arc ({X}, {Y})")

    for x in set(domains[X]):
        if all(x == y for y in domains[Y]):
            print(f"Removing {x} from {X} (no support in {Y})")
            domains[X].remove(x)
            revised = True

    if not revised:
        print("No change")

    print(f"  Domain[{X}] = {domains[X]}")
    return revised


def ac3():
    queue = [(Xi, Xj) for Xi in variables for Xj in neighbors[Xi]]

    step = 1
    while queue:
        Xi, Xj = queue.pop()
        print(f"\n=== STEP {step} ===")
        step += 1

        if revise(Xi, Xj):
            if not domains[Xi]:
                print(" Domain empty -> Failure")
                return False

            for Xk in neighbors[Xi]:
                if Xk != Xj:
                    print(f"Adding ({Xk}, {Xi}) to queue")
                    queue.append((Xk, Xi))

    print("\nAC-3 Completed Successfully")
    return True


print("Initial Domains:", domains)
intial_domain=copy.deepcopy(domains)
ac3()
print("\nFinal Domains:", domains)


if(intial_domain==domains):
    print("this problem is not arc-consistent.")