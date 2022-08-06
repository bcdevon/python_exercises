word = input("guess 5 letter word ")
text = "atone"


# X means wrong letter and place.
# ? means wrong place.
# ! means right letter and place.
def evaluate_word(guess, answer):
    if guess == answer:
        result = "!!!!!"
    if guess[0] == answer[0]:
        result = "!"
    elif guess[0] in answer:
        result = "?"
    else:
        result = "X"

    if guess[1] == answer[1]:
        result += "!"
    elif guess[1] in answer:
        result += "?"
    else:
        result += "X"

    if guess[2] == answer[2]:
        result += "!"
    elif guess[2] in answer:
        result += "?"
    else:
        result += "X"

    if guess[3] == answer[3]:
        result += "!"
    elif guess[3] in answer:
        result += "?"
    else:
        result += "X"

    if guess[4] == answer[4]:
        result += "!"
    elif guess[4] in answer:
        result += "?"
    else:
        result += "X"
    print(result)


evaluate_word(word, text)
