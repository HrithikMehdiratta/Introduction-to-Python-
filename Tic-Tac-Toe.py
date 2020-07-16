#Milestone Project- 1 
#Tic-Tac-Toe
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+'   |   '+board[2]+'   |   '+board[3])
    print('-----------------')
    print(board[4]+'   |   '+board[5]+'   |   '+board[6])
    print('-----------------')
    print(board[7]+'   |   '+board[8]+'   |   '+board[9])
def player_input():
    
    a=''
    
    while True:
        
        a=input("Player 1: Please define your choice of marker: 'X' or 'O' ")
        
        if a.upper()=='X'or a.upper()=='O':
            
            break
            
        else:
            
            print(" Please enter a valid choice")
            
    if a.upper()=='X':
        player1='X'
        player2='O'
            
            
         
        
    else:
        player1='O'
        player2='X'
        
    return(player1,player2)
    
    
def place_marker(board,marker,position):
    
        board[position]=marker
    
def win_check(board,mark):
    
    return board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark or board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark or board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark
        
    

import random 

def choose_first():
    
    first = random.randint(1,2)
    
    if first==1:
        
        return 'Player 1'           
    
    else:
        
        return 'Player 2'
    
def space_check(board,position):
    
    return board[position]==' '

def full_board_check(board):
    
    b=0
    
    for x in range(1,10):
        
        if board[x] == 'X' or board[x]== 'O':
            
            b=b+1
            
    return b==9
    
def player_choice(board):
    
    while True:
        
        position=int(input("Enter your next position  (1-9)"))
                
        free = space_check(board,position)
        
        if free:
            
            break
            
        else:
            
            print(" Position Occupied ")
            
    return position
    
def replay():
    
    again=input("Want to play again ?")
    
    if again.capitalize()=='Yes':
        
        return True
    
    else:
        
        print("Thank You for playing. See you soon!!)
              
print("Welcome to Tic-Tac-Toe!!!!")

while True:
    
    player1,player2 = player_input()
    
    player = choose_first()
    
    print(f' {player} will go first')
    
    while True:
        
        ready=input(" Are you ready ? ")
        
        if ready.capitalize()=='Yes':
            
            board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']  
            display_board(board)
            
            break
            
    game_on=True
    
    while game_on:
        
        if full_board_check(board):
            
            print(" It is a Draw !!")
            break
        
        while player=='Player 1':
            
            
            pos=player_choice(board)
            place_marker(board,player1,pos)
            display_board(board)
                
            if win_check(board,player1):
                    
                print(f'Congratulations {player} !! You won!!')
                    
                game_on = False
                    
                break
                    
            player='Player 2'
                    
        while player=='Player 2':
                
            pos=player_choice(board)
            place_marker(board,player2,pos)
            display_board(board)
                
            if win_check(board,player2):
                    
                print(f'Congratulations {player} !! You Won!!')
                    
                game_on= False
                    
                break
                    
            player='Player 1'
        
   
    if not replay():
        break


