import itertools

class Symbol:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


def NOT(p): return not p
def AND(p, q): return p and q
def OR(p, q): return p or q
def IMPLIES(p, q): return (not p) or q
def IFF(p, q): return p == q


def truth_table(expr_func, symbols, title):
    print(f"\n=== {title} ===")
    print(" | ".join([s.name for s in symbols]) + " | Result")
    print("-" * (len(symbols) * 6 + 10))

    for values in itertools.product([False, True], repeat=len(symbols)):
        val_dict = dict(zip(symbols, values))
        result = expr_func(val_dict)

        row = " | ".join(['T' if val_dict[s] else 'F' for s in symbols])
        print(f"{row} | {'T' if result else 'F'}")


P = Symbol('P')
Q = Symbol('Q')
R = Symbol('R')


truth_table(lambda v: NOT(v[P]) != v[Q], [P, Q], "~P XOR Q")
truth_table(lambda v: AND(NOT(v[P]), NOT(v[Q])), [P, Q], "~P AND ~Q")
truth_table(lambda v: OR(NOT(v[P]), NOT(v[Q])), [P, Q], "~P OR ~Q")
truth_table(lambda v: IMPLIES(NOT(v[P]), v[Q]), [P, Q], "~P -> Q")
truth_table(lambda v: IFF(NOT(v[P]), v[Q]), [P, Q], "~P <-> Q")

truth_table(lambda v: AND(
    OR(v[P], v[Q]),
    IMPLIES(NOT(v[P]), v[Q])
), [P, Q], "(P OR Q) AND (~P -> Q)")

truth_table(lambda v: IMPLIES(
    OR(v[P], v[Q]),
    v[R]
), [P, Q, R], "(P OR Q) -> R")

truth_table(lambda v: IFF(
    IMPLIES(OR(v[P], v[Q]), v[R]),
    IMPLIES(AND(NOT(v[P]), NOT(v[Q])), NOT(v[R]))
), [P, Q, R], "((P OR Q) -> R) <-> ((~P AND ~Q) -> ~R)")

truth_table(lambda v: IMPLIES(
    AND(IMPLIES(v[P], v[Q]), IMPLIES(v[Q], v[R])),
    IMPLIES(v[P], v[R])
), [P, Q, R], "((P->Q) AND (Q->R)) -> (P->R)")

truth_table(lambda v: IMPLIES(
    IMPLIES(v[P], OR(v[Q], v[R])),
    AND(NOT(v[P]), AND(NOT(v[Q]), NOT(v[R])))
), [P, Q, R], "(P -> (Q OR R)) -> (~P AND ~Q AND ~R)")