game_board =   [
                [' ','x',' '],
                [' ','x',' '],
                [' ','x',' '],
            ]
def is_there_winner(game_board):
    check = False
    winner = []
    #first column 
    if game_board[0][0] != ' ' and game_board[0][0] == game_board[1][0] and game_board[2][0] == game_board[0][0]:
        # winner.append(game_board[0][0])
        check = True
    #second column
    elif game_board[0][1] != ' ' and game_board[0][1] == game_board[1][1] and game_board [0][1] == game_board[2][1]:
        # winner.append(game_board[0][1])
        check = True
    #third column
    elif game_board[0][2] != ' ' and game_board[0][2] == game_board[1][2] and game_board[2][2] == game_board [0][2]:
        # winner.append(game_board[0][2])
        check = True
    #first row
    elif game_board[0][0] != ' ' and game_board[0][0] == game_board[0][1] and game_board[0][2] == game_board[0][0]:
        # winner.append(game_board[0][0])
        check = True
    #second row
    elif game_board[1][0] != ' ' and game_board[1][0] == game_board[1][1] and game_board[1][2] == game_board[1][0]:
        # winner.append(game_board[1][0])
        check = True
    #third row
    elif game_board[2][0] != ' ' and game_board[2][0] == game_board[2][1] and game_board[2][2] == game_board[2][0]:
        # winner.append(game_board[2][0])
        check = True
    #diagonal start top left
    elif game_board[0][0] != ' ' and game_board[0][0] == game_board[1][1] and game_board[2][2] == game_board[0][0]:
        # winner.append(game_board[0][0])
        check = True
    #diagonal start top right
    elif game_board[0][2] != ' ' and game_board[0][2] == game_board[1][1] and game_board[2][0] == game_board[0][2]:
        # winner.append(game_board[0][2])
        check = True
    print(check)
is_there_winner(game_board)
    



def get_winner():
    if is_there_winner(game_board) == True:
        print('There is a winner but who is it?')

get_winner()




# def get_winner(game_board):
#     if is_there_winner.check == True:
#         print(is_there_winner)

# get_winner(is_there_winner)



# for y in game_board[1]:
#     if y != game_board[1][0]:
#         check = False
#     if game_board[0][1] == game_board[1][1] and game_board[2][1] == game_board[0][1]:
#         check = True
# print(check)
# for z in game_board[2]:
#     if z != game_board[2][0]:
#         check = False
#     if game_board[0][2] == game_board[1][2] and game_board[2][2] == game_board[0][2]:
#         check = True
# print(check)




    
# print(game_board)
# if (game_board[0][0] and game_board[0][1] =='x') and game_board[0][2] == 'x':
#     print('true')
# elif (game_board[1][0] and game_board[1][1] =='x') and game_board[1][2] == 'x':
#     print('true')
# elif (game_board[2][0] and game_board[2][1] =='x') and game_board[2][2] == 'x':
#     print('true')
# else:
#     print('false')
   
