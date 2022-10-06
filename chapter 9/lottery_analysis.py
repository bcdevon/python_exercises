import random

def lottery_ticket():
    counter = 1
    winner = []
    lottery = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 0, 'a', 'b', 'c', 'd', 'e']
    while counter <= 4:
        choose_winner = choice(lottery)
        winner.append(choose_winner)
        counter += 1
    return winner

def my_ticket_number():
    counter = 1
    my_ticket = []
    lottery = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 0, 'a', 'b', 'c', 'd', 'e']
    while counter <= 4:
        get_ticket = choice(lottery)
        my_ticket.append(get_ticket)
        counter += 1
    return my_ticket


winning_ticket = ['1', '4', '5', '6']
lottery = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9', '0', 'a', 'b', 'c', 'd', 'e']
run = 0
while True:
    run += 1
    if random.sample(lottery, 4) == winning_ticket:
        print(f"your ticket is a winner with the numbers {winning_ticket}")
    if run > 50000:
        break
    else:
        print(f"this is try number: {run}")





        
   

    
   



  
            


    



   
