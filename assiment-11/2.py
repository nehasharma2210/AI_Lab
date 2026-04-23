import itertools

print("Solving SEND + MORE = MONEY\n")

letters = ['S','E','N','D','M','O','R','Y']
digits = range(10)

count = 0

for perm in itertools.permutations(digits, 8):

    S,E,N,D,M,O,R,Y = perm

    # Step 1: Leading zero constraint
    if S == 0 or M == 0:
        continue

    # Step 2: Units place pruning (D + E = Y mod 10)
    if (D + E) % 10 != Y:
        continue

    # Step 3: Tens place pruning (N + R + carry)
    carry1 = (D + E) // 10
    if (N + R + carry1) % 10 != E:
        continue

    count += 1

    # Show progress (not too much printing)
    if count % 200 == 0:
        print("Checked", count, "cases...")

    # Step 4: Form numbers
    SEND = S*1000 + E*100 + N*10 + D
    MORE = M*1000 + O*100 + R*10 + E
    MONEY = M*10000 + O*1000 + N*100 + E*10 + Y

    # Step 5: Final check
    if SEND + MORE == MONEY:
        print("\nSolution Found")
        print(f"{SEND} + {MORE} = {MONEY}")
        print("Mapping:")
        print(f"S={S}, E={E}, N={N}, D={D}, M={M}, O={O}, R={R}, Y={Y}")
        print(f"answer found in {count} permutation")
        break