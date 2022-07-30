diners = input("How many people are in your group? ")
diners = int(diners)
if diners > 8:
    print("Im sorry you'll have to wait for a table")
elif diners <= 8:
    print("Your table is ready")
