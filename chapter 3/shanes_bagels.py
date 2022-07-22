instructions = "I am thinking of a 3-digit number. Try to guess what it is.\n"
instructions += "When I say wrong: that means one digits is correct but in the wrong positon.\n"
instructions += "When I say good: one digit is right and in the right positon"
answer = '123'
print(instructions)
for counter in range(1, 11):
    guess = input("%d Enter 3 digit number: " % counter)
    print(guess)
    if answer == guess:
        print("correct")
    if answer[0] == guess[0]:
        print("good")
    elif guess[0] in answer:
        print("illplaced")
    else:
        print("wrong")
    if answer[1] == guess[1]:
        print("good")
    elif guess[1] in answer:
        print("illplaced")
    else:
        print("wrong")
    if answer[2] == guess[2]:
        print("good")
    elif guess[2] in answer:
        print("illplaced")
    else:
        print("wrong")
   