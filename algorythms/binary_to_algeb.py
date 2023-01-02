def binary_to_algeb(polynom: list[int]) -> str:
    text: str = ""

    for index in range(1, len(polynom)+1):
        if polynom[-index]:
            if index > 2:
                char: str = "x^" + str(index-1)
            elif index == 2:
                char: str = "x"
            else:
                char: str = "1"

            if text != "":
                text = char + " + " + text
            else:
                text = char

    return text


if __name__ == '__main__':
    print(binary_to_algeb([1, 0, 1, 1]))
