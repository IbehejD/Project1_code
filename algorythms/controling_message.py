from algorythms.xor_polynoms import xor_polynoms


def control_message(message: list[int], gen_polynom: list[int]) -> bool:
    '''Methot controling if message is correct'''
    # remainder aftere control polynom divison
    remainder: list[int] = xor_polynoms(message, gen_polynom)
    # control of remainder
    for value in remainder:
        if value:
            return False, remainder

    return True


if __name__ == '__main__':
    message = [1, 0, 1, 0, 1, 0, 1, 0]
    gen_polynom = [1, 1, 0, 1]

    print(control_message(message, gen_polynom))
