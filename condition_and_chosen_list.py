from number_generator import lucky_numbers, even_numbers
from random import sample, randint
def list_generator(amount):
    chosen_list = []
    even_list = even_numbers(amount)
    lucky_list = lucky_numbers(amount)
    am_even = randint(1, amount//2)
    am_lucky = randint(1,(amount//2)-1)
    chosen_even = sample(even_list, am_even)
    chosen_lucky = sample(lucky_list, am_lucky)
    chosen_list = chosen_even + chosen_lucky
    return chosen_list

def condition_generator():
    condition_list = ['even', 'Ulam', 'lucky']
    condition = sample(condition,1)
    return condition

