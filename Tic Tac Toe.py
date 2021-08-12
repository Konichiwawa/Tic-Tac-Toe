import random 

print('Welcome to Tic Tac Toe!')

# the board 
The_board = ['0','','','','','','','','','']

# function to display the board  
def display(board):
    
    print(board[1], '|', board[2], '|', board[3])
    print('-', '-', '-', '-')
    print(board[4], '|', board[5], '|', board[6])
    print('-', '-', '-', '-')
    print(board[7], '|', board[8], '|', board[9])

# function to select players
def choose_player():
    
    try:  
        player = input('Are you X or O?: ').upper
    except:
        print('enter X or O')
    else:
        if player == 'X':
            return ('X','O')
        else:
            return ('O','X')
    
# randomly chooses who goes first  
def choose_turn():
    
    if random.randint(0,1) == 0:
        return 'player1'
    else:
        return 'player2'
    
# let players choose their position 
def choose_position():
    
    position = 0
    
    while position not in range(1,10):
        
        try:
            position = int(input('Choose your position 1-9: '))
        except:
            print('Enter only an interger from 1 to 9')
        else:
            break
        
    return position

# check if the chosen position is empty or taken
def check_position(board, position):
    
    if board[position] == '' and board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False 
    
# check the board for empty positions
def check_board(board):
    
    for i in range(1,10):
        
        if i == '':
            return True
        else:
            return False 
        
# check for win
def check_win(board, player):
    
    return (
    (board[1] == player and board[2] == player and board[3] == player) or
    (board[4] == player and board[5] == player and board[6] == player) or 
    (board[7] == player and board[8] == player and board[9] == player) or 
    (board[1] == player and board[4] == player and board[7] == player) or 
    (board[2] == player and board[5] == player and board[8] == player) or
    (board[3] == player and board[6] == player and board[9] == player) or 
    (board[1] == player and board[5] == player and board[9] == player) or 
    (board[3] == player and board[5] == player and board[7] == player)
    )

# check for tie
def check_tie(board, player):
    
    return check_win(board, player) == False and check_board(board) == True
    
# ask to play again
def ask_replay():
    
    while True:
        try:
            replay = input('Would you like to play again? Y/N: ').upper()
        except:
            print('enter Y or N')
        else:
            if replay == 'Y':
                return True
                break
            else:
                return False
                break

# game logic 
while True:
    
    # player & turn selection 
    player1, player2 = choose_player()
    turn = choose_turn()
    
    play = False 
    
    # randomly assigns player1 & 2 then initiate the game 
    if turn == 'player1':
        print(player1, ' goes first')
        play = True 
    elif turn == 'player2':
        print(player2, ' goes first')
        play = True 
    
    while play == True:
        
        # this if statement controls player1
        if turn == 'player1':
            
            display(The_board)
            position = choose_position()
            
            while True:
                if check_position(The_board, position) == True:
                    The_board[position] = player1
                    break
                else:
                    print('position is already taken')
            
            if check_win(The_board, player1) == True:
                display(The_board)
                print(player1 + ' wins!')
                play = False
                break
            
            if check_tie(The_board, player1) == True:
                display(The_board)
                print("It's tie!")
                play = False
                break
                
            # swtich turn
            turn = 'player2'
            print(player2, "'s turn")
               
        # this if statement controls player2
        elif turn == 'player2':
            
            display(The_board)
            position = choose_position()
            
            while True:
                if check_position(The_board, position) == True:
                    The_board[position] = player2
                    break
                else:
                    print('position is already taken')
        
            if check_win(The_board, player2) == True:
                display(The_board)
                print(player2 + ' wins!')
                play = False
                break
            
            if check_tie(The_board, player2) == True:
                display(The_board)
                print("It's tie!")
                play = False 
                break
            
            # swtich turn
            turn = 'player1'
            print(player1, "'s turn")
            
    if play == False:
        replay = ask_replay()
        if replay == True:
            The_board = ['0','','','','','','','','','']
            continue
        else:
            print('Thanks for playing!')
            break