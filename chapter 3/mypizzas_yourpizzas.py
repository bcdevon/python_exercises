pizzas =["pepperoni", "bbq chicken", "zinger"]

for pizza in pizzas:
    print(f"I like {pizza} pizza!")
print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('cheese')
friend_pizzas.append('sausage')

for pizza in pizzas:
    print(f"My favorite pizzas are:{pizza}")
print("\n")
for friend_pizza in friend_pizzas:
    print(f"My favorite pizzas are:{friend_pizza}")
