def xor_polynoms(divident: list[int], divisor: list[int]) -> list[int]:
    '''Method appliing XOR on two polynoms'''
    #convertion to bool values to make it faster
    divident: list[bool] = [bool(i) for i in divident]
    divisor: list[bool] = [bool(i) for i in divisor]

    for i, value_i in enumerate(divident):
        #condition handling move of start division
        if value_i:
            #ending condition
            if (len(divident) - i) >= len(divisor): 
                for j, value_j in enumerate(divisor):
                    divident[j + i] = divident[j + i] != value_j
            else:
                break
    #convertion back to int values
    divident: list[int] = [int(i) for i in divident]

    return divident

if __name__ == '__main__':
    divident = [1,0,1,0,0,0,0,0]
    divisor = [1,1,0,1]

    print(xor_polynoms(divident, divisor))