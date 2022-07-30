prompt = "\nHow old are you "
counter = 1

while counter <= 5:
    counter += 1
    age = input(prompt)

    if age == 'quit':
        break
    elif int(age) < 3:
        print("Your ticket is free ")
    elif int(age) <= 12:
        print("Your ticket is $10.00")
    elif int(age) > 12:
        print("Your ticket is $15.00")
