import random


a_list = ['33','18','27','5','4','12']

winner_ticket = ['33','18','27', '12']
run = 0 
while True:
    run += 1
    if random.sample(a_list,4) == winner_ticket:
        print(f"Your ticket is a winner with the numbers d{winner_ticket}")
        break

    if run > 50000:
            break
    else:
        print(f"This is try number: {run}")