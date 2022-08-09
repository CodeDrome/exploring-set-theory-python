
import setutilities as su


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Set Demo      |")
    print("-----------------\n")

    # print(su.symbols)

    # create_and_manipulate()

    # builtins()

    # cardinality_string()

    # tests_and_comparisons()

    # combinations()

    # update()


def create_and_manipulate():

    A = set()
    print(A)

    A.add(98)
    print(A)

    A.update([101, 103, 108])
    print(A)

    n = A.pop()
    print(n)
    print(A)

    try:
        A.remove(103)
    except KeyError as err:
        print(err)
    else:
        print("element 103 removed")

    print(A)

    try:
        A.remove(103)
    except KeyError as err:
        print("element not in set")
    else:
        print("103 removed")

    print(A)

    # does not raise exception if element not present
    A.discard(103)

    print(A)

    # clear
    A.clear()
    print(A)


def builtins():

    title = "Selection of built in functions applied to set"
    print(title)
    print("-" * len(title))

    A = {7,-67,85,-86,4,0}

    print(f"set A    {A}")

    print(f"len(A)   {len(A)}")
    print(f"min(A)   {min(A)}")
    print(f"max(A)   {max(A)}")
    print(f"sum(A)   {sum(A)}")
    print(f"all(A)   {all(A)}")
    print(f"any(A)   {any(A)}")

    B = set(filter(lambda n: n > 0, A))
    print(f"filter   {B}")

    P = set(map(lambda n: n ** 2, A))
    print(f"map      {P}")


def cardinality_string():

    s = {7,-67,85,-86,4,0}

    cs = su.cardinality_string(s, "myset")

    print(cs)


def tests_and_comparisons():

    A = {1,2,4,7,9,13,16,22}
    B = {1,2,4,7}
    C = {3,5,6,8}

    print(f"is element of\n9 {su.symbols['is_element_of']} {A}\n{9 in A}\n")

    print(f"is not element of\n3 {su.symbols['is_not_element_of']} {A}\n{3 not in A}\n")

    print(f"is disjoint\n{A} {su.symbols['intersection']} {B} = {su.symbols['emptySet']}\n{A.isdisjoint(B)}\n")

    print(f"is subset of\n{B} {su.symbols['is_subset_of']} {A}\n{B.issubset(A)}\n") # or B <= A

    print(f"is proper subset of\n{B} {su.symbols['is_proper_subset_of']} {A}\n{B < A}\n")
    # no method for proper subset, can only use <

    print(f"is superset of\n{A} {su.symbols['is_superset_of']} {B}\n{A.issuperset(B)}\n") # or A >= B

    print(f"is proper superset of\n{A} {su.symbols['is_proper_superset_of']} {B}\n{A > B}\n")
    # no method for proper superset, can only use >


def combinations():

    A = {1,2,4,7,9}
    B = {1,2,4,8,10}

    U = A.union(B)
    # or U = A | B

    I = A.intersection(B)
    # or I = A & B

    D = A.difference(B)
    # or D = A - B

    S = A.symmetric_difference(B)
    # or D = A ^ B

    print(f"{A} {su.symbols['union']} {B} = {U}")
    print(f"{A} {su.symbols['intersection']} {B} = {I}")
    print(f"{A} {su.symbols['set_difference']} {B} = {D}")
    print(f"{A} {su.symbols['symmetric_difference']} {B} = {S}")


def update():

    A = {1,2,3,4}
    B = {4,5,6,7}
    C = {5,6,7,8,9}
    D = {7,8,9,10}
    E = {6,11,12}

    print(f"A = {A}\n")

    # A is now union of itself and B
    print(f"{A}.update({B})")
    A.update(B) # or |=
    print(f"= {A}\n")

    # A now contains only elements in itself and C
    print(f"{A}.intersection_update({C})")
    A.intersection_update(C) # or &=
    print(f"= {A}\n")

    # A now contains only elements not also in D
    print(f"{A}.difference_update({D})")
    A.difference_update(D) # or -=
    print(f"= {A}\n")

    # A now contains elements in itself but not E, and in E but not itself
    print(f"{A}.symmetric_difference_update({E})")
    A.symmetric_difference_update(E) # or ^=
    print(f"= {A}\n")


if __name__ == "__main__":
    main()
