from itertools import product
from algorythms.xor_polynoms import xor_polynoms



def is_polynom(n: int, gen_polynom: list[int]):
    # polynom which will be divitet to check if polynom is genering polynom
    control_polynom: list[int] = generate_control_polynom(n)
    # remainder aftere control polynom divison
    remainder: list[int] = xor_polynoms(control_polynom, gen_polynom)
    # control of remainder
    for value in remainder:
        if value:
            return False

    return True


def generate_control_polynom(n: int) -> list[int]:
    control_polynom: list[int] = [0] * (n+1)
    control_polynom[0] = 1
    control_polynom[-1] = 1

    return control_polynom


def find_polynoms(n: int, k: int) -> list[list[int]]:
    gen_polynoms: list[list[int]] = []

    # generating polynoms of n-order
    for polynom in product([True, False], repeat=(n-k)):
        # convertion to list and appending 1 to first position to have polynom of n-order
        polynom = list(polynom)
        polynom.insert(0, True)

        # condition to add polynom into gen_polynoms
        if is_polynom(n, polynom):
            gen_polynoms.append([int(i) for i in polynom])

    return gen_polynoms


if __name__ == '__main__':
    print(find_polynoms(7, 4))
