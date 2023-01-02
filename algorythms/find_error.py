from algorythms.xor_polynoms import xor_polynoms
from algorythms.binary_to_algeb import binary_to_algeb
from algorythms.controling_message import control_message

def find_error(message, gen_polynom, symptom):
    control_polynom_generator = generate_control_polynom(len(message))

    for polynom in control_polynom_generator:
        remain = xor_polynoms(polynom, gen_polynom)
        if remain == symptom:
            print(polynom)
            return polynom

def repair_message(message, polynom):
    for index, value in enumerate(polynom):
        if value:
            message[index] = int(not(message[index]))

    return message

def generate_control_polynom(n):
    control_polynom: list[int] = [0] * (n)
    control_polynom[0] = 1
    index = 0
    while index <= n:
        yield control_polynom
        if index < n:
            control_polynom[index],control_polynom[index + 1] = control_polynom[index + 1], control_polynom[index]
        index += 1

if __name__ == '__main__':
    message = [1,0,1,0,1,0,1,0]
    gen_polynom = [1,1,0,1]
    symptom = control_message(message, gen_polynom)
    error = find_error(message, gen_polynom, symptom[1])
    correct_message = repair_message(message, error)
    print(binary_to_algeb(error))
    print(correct_message)
    print(binary_to_algeb(correct_message))