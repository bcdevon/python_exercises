import random

def get_deck():
    return ['HA', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'CA', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'SA', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK'] 
def draw_card(num_cards):
    cards_drawn = []
    deck = get_deck()
    for i in range(0, num_cards):
        random_number = random.randint(0, 51-i)
        random_card = deck[random_number]
        del deck[random_number]
        cards_drawn.append(random_card)
    return cards_drawn
card = draw_card(3)
print(card)
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
        
print(calculate_hand(card, True))




