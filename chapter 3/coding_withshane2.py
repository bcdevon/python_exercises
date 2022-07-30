# numbers = [1, 5, 10, 13]
# usr_number = input('enter your number')
# usr_number = int(usr_number)
# for i in range(0, len(numbers)):
#     if usr_number < numbers[i]:
#         print('number is too big')

import random

def create_random_list():
    random_list = []
    list_length = random.randint(0, 5)

    for i in range(0, list_length):
        random_list.append(random.randint(0, 100))

    return random_list

nums = create_random_list()
print(nums)

def find_max_number(num_list):
    if len(num_list) == 0:
        return 'empty list'
    max = num_list[0]
    for i in range(0, len(num_list)):
        if max < num_list[i]:
            max = num_list[i]
    return max
print(find_max_number([]))
