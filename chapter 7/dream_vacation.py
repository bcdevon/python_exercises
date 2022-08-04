responses = {}
polling_active = True
prompt = "If you could visit one place in the world, where would you go? "

while polling_active:
    name = input("\nWhat is your name")
    response = input(prompt)
    responses[name] = response
    next_person = input("Would you like to let another person respond (Yes/No)")
    if next_person == 'No':
        polling_active = False

    print("\n---Polling Results---")
    for name, response in responses.items():
        print(f"{name} wants to visit {response}.")
