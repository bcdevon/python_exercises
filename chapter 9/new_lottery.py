import random

winning_ticket = ['1', '4', '5', 'a']
lottery = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9', '0', 'a', 'b', 'c', 'd', 'e']

run = 0 
while True:
    run += 1
    if random.sample(lottery,4) == winning_ticket:
         print(f"Your ticket is a winner with the numbers d{winning_ticket}")
         break

    if run > 90000:
            break
    else:
        print(f"This is try number: {run}")
