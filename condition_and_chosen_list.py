from number_generator import lucky_numbers, even_numbers
from random import sample, randint
def list_generator(amount: int)-> list:
    '''
    am_even,am_lucky,am_ulam - random amounts of numbers from lists
    chosen_even,chosen_lucky,chosen_ulam - sub lists of generated numbers
    chosen_list - final list
    '''
    chosen_list = []
    even_list = even_numbers(amount)
    lucky_list = lucky_numbers(amount)
    am_even = randint(1, amount//2)
    am_lucky = randint(1,(amount//2)-1)
    am_ulam = amount - am_even - am_lucky
    chosen_even = sample(even_list, am_even)
    chosen_lucky = sample(lucky_list, am_lucky)
    chosen_ulam = sample(ulam_list, am_ulam)
    chosen_list = chosen_even + chosen_lucky + chosen_ulam
    return chosen_list

def condition_generator()->str:
    '''
    this function randomly generates one of the 3 conditions
    '''
    condition_list = ['even', 'Ulam', 'lucky']
    condition = sample(condition,1)
    return condition

