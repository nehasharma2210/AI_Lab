# =========================================
# AI Assignment: FC + BC + Resolution
# (WITH STEP PRINTING, WINDOWS SAFE)
# =========================================

# ================================
# 1. FORWARD CHAINING
# ================================
def forward_chaining(rules, facts, goal):
    inferred = set(facts)
    print("\nInitial Facts:", inferred)

    step = 1
    while True:
        added = False
        for premise, conclusion in rules:
            print(f"\nStep {step}: Checking {premise} -> {conclusion}")

            if all(p in inferred for p in premise):
                if conclusion not in inferred:
                    print(f"  [OK] Fired! Adding {conclusion}")
                    inferred.add(conclusion)
                    added = True
                else:
                    print(f"  -> Already known: {conclusion}")
            else:
                missing = set(premise) - inferred
                print(f"  [NO] Cannot fire (missing {missing})")

            step += 1

        if not added:
            break

    print("\nFinal Facts:", inferred)
    return goal in inferred


# ================================
# 2. BACKWARD CHAINING
# ================================
def backward_chaining(rules, facts, goal, depth=0):
    indent = "  " * depth
    print(f"{indent}Goal: {goal}")

    if goal in facts:
        print(f"{indent}[OK] Found in facts")
        return True

    for premise, conclusion in rules:
        if conclusion == goal:
            print(f"{indent}Trying rule: {premise} -> {conclusion}")

            if all(backward_chaining(rules, facts, p, depth+1) for p in premise):
                print(f"{indent}[OK] Rule satisfied for {goal}")
                return True

    print(f"{indent}[NO] Failed to prove {goal}")
    return False


# ================================
# 3. RESOLUTION
# ================================
def resolve(ci, cj):
    resolvents = []
    for di in ci:
        for dj in cj:
            if di == ('~' + dj) or ('~' + di) == dj:
                new_clause = set(ci + cj)
                new_clause.discard(di)
                new_clause.discard(dj)
                resolvents.append(tuple(new_clause))
    return resolvents


def resolution(kb, query):
    clauses = kb + [(f"~{query}",)]
    print("\nInitial Clauses:", clauses)

    step = 1
    while True:
        new = []
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                print(f"\nStep {step}: Resolving {clauses[i]} and {clauses[j]}")
                resolvents = resolve(clauses[i], clauses[j])
                print("  Resolvents:", resolvents)

                if () in resolvents:
                    print("  [OK] Empty clause found (PROVED)")
                    return True

                new.extend(resolvents)
                step += 1

        if set(new).issubset(set(clauses)):
            print("\n[NO] No new clauses (NOT PROVED)")
            return False

        clauses.extend(new)
        print("\nUpdated Clauses:", clauses)


# ================================
# MAIN PROGRAM
# ================================
if __name__ == "__main__":

    print("===== FORWARD CHAINING =====")

    # (a)
    rules_fc1 = [
        (["P"], "Q"),
        (["L", "M"], "P"),
        (["A", "B"], "L")
    ]
    facts_fc1 = ["A", "B", "M"]

    print("\n--- FC (a) ---")
    result = forward_chaining(rules_fc1, facts_fc1, "Q")
    print("\nFinal Result Q:", result)

    # (b)
    rules_fc2 = [
        (["A"], "B"),
        (["B"], "C"),
        (["C"], "D"),
        (["D", "E"], "F")
    ]
    facts_fc2 = ["A", "E"]

    print("\n--- FC (b) ---")
    result = forward_chaining(rules_fc2, facts_fc2, "F")
    print("\nFinal Result F:", result)


    print("\n\n===== BACKWARD CHAINING =====")

    # (a)
    rules_bc1 = [
        (["P"], "Q"),
        (["R"], "Q"),
        (["A"], "P"),
        (["B"], "R")
    ]
    facts_bc1 = ["A", "B"]

    print("\n--- BC (a) ---")
    result = backward_chaining(rules_bc1, facts_bc1, "Q")
    print("\nFinal Result Q:", result)

    # (b)
    rules_bc2 = [
        (["A"], "B"),
        (["B", "C"], "D"),
        (["E"], "C")
    ]
    facts_bc2 = ["A", "E"]

    print("\n--- BC (b) ---")
    result = backward_chaining(rules_bc2, facts_bc2, "D")
    print("\nFinal Result D:", result)


    print("\n\n===== RESOLUTION =====")

    # (a)
    kb1 = [
        ("P", "Q"),
        ("~P", "R"),
        ("~Q", "S"),
        ("~R", "S")
    ]

    print("\n--- RES (a) ---")
    result = resolution(kb1, "S")
    print("\nFinal Result S:", result)

    # (b)
    kb2 = [
        ("~P", "Q"),
        ("~Q", "R"),
        ("~S", "~R"),
        ("P",)
    ]

    print("\n--- RES (b) ---")
    result = resolution(kb2, "S")
    print("\nFinal Result S:", result)