found_negative = False
sum = 0
while found_negative == False:
    num = input("Enter a number: ")
    num = int(num)
    if num >= 0:
        sum += num
        print(num)
    elif num < 0:
        found_negative = True
        print(sum)