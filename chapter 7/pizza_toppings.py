prompt = "\nWhat toppings do you want? "
topping_limit = 1

while topping_limit <= 10:
    topping_limit += 1
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza")
