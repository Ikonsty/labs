def division_of_two(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False


print(division_of_two(int(input()), int(input())))
