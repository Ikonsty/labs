import doctest


def generate_number(number, digit, position):
    '''this function changes the digit in a given number
    if given digit is bigger than the digit in the given position
     (int) -> int
    Precondition: 0 < digit < 9 
    >>> generate_number(3746, 5, 0)
    3746
    >>> generate_number(3746, 5, 1)
    3756
    >>> generate_number(3746, 5, 2)
    3746
    '''
    len_number = 0
    n = int(number)
    while (abs(n) > 0):
        n = abs(n) // 10
        len_number += 1

    number = int(number)
    digit = int(digit)
    position = int(position)

    reminder = abs(number) % (10 ** position)
    previous_digits = abs(number) // (10 ** (position + 1)
                                      ) * 10 ** (position + 1)
    if position > len_number:
        new_number = digit*10**position + abs(number)
        if number == abs(number):
            return new_number
        else:
            return -1*new_number
    else:
        if ((abs(number) - previous_digits - reminder) / 10 ** position) >= digit:
            return number
        else:
            new_number = previous_digits + digit * 10 ** position + reminder
            if number == abs(number):
                return new_number
            else:
                return -1*new_number


doctest.testmod()
