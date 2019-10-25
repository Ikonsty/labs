
def even_numbers(amount):
    even_list=[]
    for i in range(amount):
        if i % 2 == 0:
            even_list.append(i)
    return even_list

def lucky_numbers(amount):
    lucky_list = list(range(1, amount + 1, 2)); j = 1
    while lucky_list[j] <= len(lucky_list)-1:
        lucky_list = [lucky_list[i] for i in range(len(lucky_list))\
            if (i + 1) % lucky_list[j] != 0]
        j+=1
    return(lucky_list)

import random
max = 100
arr = []
ul_arr = []
def ulam(amount):
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
