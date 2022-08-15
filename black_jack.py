import random
import sys

def get_deck():
    deck = ['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK'] 
    random.shuffle(deck)
    return deck

def draw_card(deck, initial_hand=False):
    cards_drawn = []
    if initial_hand:
        cards_drawn.append(deck.pop())
    cards_drawn.append(deck.pop())
    return cards_drawn

card_values = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}
def calculate_hand(cards_drawn, ace_is_1 = False):
    total = 0
    for card in cards_drawn:
        key = card[1:]
        if key == 'A' and ace_is_1:
            total += 1
        else:
            total += card_values[key]
    return total
        

def display_controls():
    print('controls H S Q')

def play():
    user_input = ''
    while user_input != 'q':
        #deck = draw 52 random cards
        deck = get_deck()
        #draw 2 cards for dealer in list and 2 cards for user in list 3rd list for deck
        dealer_hand = draw_card(deck, initial_hand=True)
        player_hand = draw_card(deck, initial_hand=True)
        #loop bust or stay. everything in loop probably in function named turn
        player_hand_value = calculate_hand(player_hand)
        while player_hand_value <= 21:
            print(player_hand_value)
            #print to user controls
            display_controls()
            #get user input
            user_input = input() 
            #evaluate input
            if user_input == 's':
                break
            elif user_input == 'q':
                sys.exit('game over')
            else:
                player_hand.extend(draw_card(deck))
                player_hand_value = calculate_hand(player_hand)
        #end loop

        #dealers turn function
        #evaluate hands 
        
play()





