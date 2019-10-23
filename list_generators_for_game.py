def even_numbers(amount):
    even_list=[]
    for i in range(amount):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

def is_happy(a):
    result = 0 
    while(a > 0):
        x = a%10
        a //= 10
        result += x**2
    return result

def happy_numbers(amount):
    happy_list = [1]
    for result in range(2,amount):
        result1 = result
        while result1 != 1 and result1 != 4:
            result1 = is_happy(result1)
            if result1 == 1:
                happy_list.append(result)
                break
            if result1 == 4:
                break
    return happy_list

def lucky_numbers(amount):
    lucky_list = list(range(1, amount + 1, 2)); j = 1
    while lucky_list[j] <= len(lucky_list)-1:
        lucky_list = [lucky_list[i] for i in range(len(lucky_list)) if (i + 1) % lucky_list[j] != 0]
        j+=1
    return(lucky_list)
print(lucky_numbers(100))       
         

def lucky(number):
    l = range(1, number + 1, 2)
    i = 1
    while i < len(l):
        del l[l[i] - 1::l[i]]
        i += 1
    return l

print(lucky(100))
