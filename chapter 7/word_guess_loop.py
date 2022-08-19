word = input("guess 5 letter word ")
text = "atone"


# X means wrong letter and place.
# ? means wrong place.
# ! means right letter and place.
def evaluate_word(guess, answer):
  
    for i in range(len(guess)):
        for j in range(len(answer)):
            if guess == answer:
                result = "!!!!!"
            elif guess[i] == answer[j]:
                result += "!"
            elif guess[i] in answer:
                result += "?"
            else: 
                result += "X"
            print(result)
evaluate_word(word, text)
