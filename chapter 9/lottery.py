from random import choice

def lottery_ticket():
    counter = 1
    winner = []
    lottery = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 0, 'a', 'b', 'c', 'd', 'e']
    while counter <= 4:
        choose_winner = choice(lottery)
        winner.append(choose_winner)
        counter += 1
    print(f"Anyone with a ticket that matches {winner} wins a prize!")

lottery_ticket()
   

