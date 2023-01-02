from algorythms.xor_polynoms import xor_polynoms


def sequre_polynom(message: list[int], gen_polynom: list[int], n: int, k: int) -> list[list[int], list[int]]:
    '''Method securing message by securing polynom'''
    s = n - k
    # expand by s bits
    [message.append(0) for _ in range(s)]
    # find secure polynom
    sequre_polynom = xor_polynoms(message, gen_polynom)
    # secure message
    for index in range(1, s + 1):
        message[-index] = sequre_polynom[-index]

    return message, gen_polynom


if __name__ == '__main__':
    message = [1, 0, 1, 0, 0]
    secure_polynom = [1, 1, 0, 1]

    print(sequre_polynom(message, secure_polynom, 7, 4))
