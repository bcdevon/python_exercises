from random import randint
class Dice:
    
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

my_turn = Dice()
my_turn.roll_die()
