import random
def even_numbers(amount):
    '''
    this function creates a list of even numbers that are less than amount
    '''
    even_1_list = []
    for i in range(100):
        if i % 2 == 0:
            even_1_list.append(i)
    even_list = []
    n = 0
    for j in range(amount):
        even_list.append(even_1_list[random.randint(0,len(even_1_list)-1)])

        
    return even_list


def lucky_numbers(amount):
    '''
    this function creates a list of lucky numbers that are less than amount
    '''
    answ = []
    lucky_list = list(range(1, amount + 1, 2)); j = 1
    while lucky_list[j] <= len(lucky_list)-1:
        lucky_list = [lucky_list[i] for i in range(len(lucky_list))
            if (i + 1) % lucky_list[j] != 0]
        j+=1
    for i in range(amount):
        n = (random.randint(1, 15))
        x = lucky_list[n - 1]
        answ.append(x)
    return answ

max = 100
arr = []
ul_arr = []
def ulam_numbers(amount):
    '''
    this function creates a list of random ulam numbers, some can be repeated
    var amount is responcible for the amount of numbers in list
    '''
    s = set()
    arr.append(1)
    s.add(1)

    arr.append(2)
    s.add(2)
    for i in range(3, max):
        count = 0
        for j in range(0, len(arr)):
            # Check if i-arr[j] exist in the array or not using set. If yes, Then i can be represented as sum of arr[j] + (i- arr[j])
            if (i - arr[j]) in s and arr[j] != (i - arr[j]):
                count += 1

            if count > 2:
                break
        if count == 2:
            arr.append(i)
            s.add(i)
    for i in range(amount):
        n = int(random.uniform(1, 15))
        x = arr[n - 1]
        ul_arr.append(x)
    return ul_arr

if __name__ == "__main__":
    amount = int(input())
    print(ulam(amount))
