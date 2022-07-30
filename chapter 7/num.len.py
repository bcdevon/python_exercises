def num_len(num):
    number = len(str(num))
    if num < 0:
        print(number - 1)
    else:
        print(number)


num_len(1235)
