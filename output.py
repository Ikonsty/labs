from number_generator import lucky_numbers, even_numbers
from condition_and_chosen_list import list_generator, condition_generator

numb = input()

def true_false(condition):
    if condition == 'even':
        if (numb in even_list) and (numb in chosen_list):
            return True
        else:
            return False

    elif condition == 'lucky':
        if (numb in lucky_list) and (numb in chosen_list):
            return True
        else:
            return False
    
    else:
        if (numb in ulam_list) and (numb in chosen_list):
            return True
        else:
            return False
score = 0

def count_score(score):
    condition = condition_generator()
    if true_false(condtion) == True:
        score += 1
    else: 
        true_false(condition) == False
        score -= 1
    return score

def next_list():
    next_list = chosen_list
    next_list.remove(numb)
    A = []
    for i in chosen_list:
        if i in even_list:
            A.append(0)
        if i in lucky_list:
            A.append(1)
        if i in ulam_list:
            A.append(2)

    if (A.find(0) == -1) and (A.find(1) != -1) and (A.find(2) != -1):
        next_list.append(sample(even_list, 1))

    elif (A.find(0) != -1) and (A.find(1) == -1) and (A.find(2) != -1):
        next_list.append(sample(lucky_list, 1))

    elif (A.find(0) != -1) and (A.find(1) != -1) and (A.find(2) == -1):
        next_list.append(sample(ulam_list, 1))
    
    elif (A.find(0) != -1) and (A.find(1) != -1) and (A.find(2) != -1):
        B = [even_list, lucky_list, ulam_list]
        random_list = sample(B, 1)
        next_list.append(sample(random_list, 1))
    return next_list