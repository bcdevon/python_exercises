
def instructions():
    print("It is you vs the computer.There are seven sticks. You can pick up 1, 2, or 3 sticks. You cannot pass. Whoever picks up the last stick loses.")
   

# def play():
count = 0
whos_turn = ""
instructions()
turn = input("Do you want to go first?")
total_sticks = 7
if turn == "no":
        count += 1
        whos_turn = "computer"
while total_sticks > 0:
    if count%2 == 1:
         print("computers turn")
         total_sticks -= 2
         print(total_sticks)
         count += 1
         whos_turn = "computer"
         if total_sticks <= 0:
            print(f"{whos_turn} You picked up the last stick you lose.")
            break
    if count%2 != 1:
         whos_turn = "player 1"
    pick_up = input("How many sticks do you want: ")
    pick_up = int(pick_up)
    total_sticks -= pick_up
    count += 1
    print(total_sticks)
    if total_sticks <= 0:
        print(f"{whos_turn} You picked up the last stick you lose.")

    