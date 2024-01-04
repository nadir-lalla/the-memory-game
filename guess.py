import random


def main():

    print("Welcome to Picture Match\n")
    print("There are 10 'pictures' (emojis) in ROW 1 and ROW 2")
    print("The ojective of the game is to match the PICTURES in ROW 1 to the PICTURES in ROW 2")
    
    cheat = False
    r1 = ['🍇','🍊','🍋','🍏','🍆','🍄','🥟','🌎','🧡','🐶']
    r2 = ['🍇','🍊','🍋','🍏','🍆','🍄','🥟','🌎','🧡','🐶']
    remainder = len(r1)

    while True:

        # Creates a board with `~` as placeholders and prints it to begin the game
        board = ['~'] * 20
        game_board(board)

        
        print("\nFirst you have to choose how many tries you will like to have")
        tries = Tries()

        mixer(r1, r2)


        answer(cheat, r1, r2)

        while tries > 0 and remainder !=0:
        
            guess_r1 = r1_position()
            guess_r2 = r2_position()

            if r1[guess_r1] == r2[guess_r2]:
                if board[guess_r1] == r1[guess_r1]:
                    print(f'You have already matched LETTER {r1[guess_r1]}')
                else:
                    remainder = remainder - 1
                    print(f'\nCORRECT, Matched {r1[guess_r1]}\n')
                    print(f'There are {remainder} combinations left to match\n')

                    board[guess_r1] = r1[guess_r1]
                    board[guess_r2+10] = r2[guess_r2]

                    game_board(board)
                
            else:
                print('\nNo Match')
                game_board(board)
                tries = tries - 1
                if tries == 0:
                    print('\nGAME OVER')
                    print('You have ran out of tries\n')
                    answer(True, r1, r2)
                else:
                    if tries == 1:
                        print(f'(You have {tries} try left)')
                    else:
                        print(f'(You have {tries} tries left)')
                    print('\nHINT:')
                    print(f'\tROW 1 position {guess_r1+1} is {r1[guess_r1]}')
                    print(f'\tROW 2 position {guess_r2+1} is {r2[guess_r2]}\n')

            if remainder == 0:
                print('\n\nCONGRATULATIONS')
                print('You have won\n')


        if not replay():
            break


def game_board(board):
    """
    Function to print out the game board
    """
    print('\nROW 1 --- ' + board[0],'| '+board[1],'| '+board[2],'| '+board[3],'| '
          +board[4],'| '+board[5],'| '+board[6],'| '
          +board[7],'| '+board[8],'| '+board[9])
    print('--------------------------------------------------------')
    print('ROW 2 --- ' +board[10],'| '+board[11],'| '+board[12],'| '+board[13],'| '
          +board[14],'| '+board[15],'| '+board[16],'| '
          +board[17],'| '+board[18],'| '+board[19])


def Tries():
    
    tries = 0
    options = range(1,6)
    
    while tries not in options:
        try:
            tries = int(input('How many tries would you like? [1-5] '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if tries < 0:
                print('Tries cannot be NEGATIVE!!')
            elif tries == 0:
                print('Tries cannot be ZERO')
        if tries not in options:
            print(f'Sorry, Please enter a number between 1 and {options[-1]}')
        if tries in options:
            if tries == 1:
                print(f'You have {tries} try to win the game\n')
            else:
                print(f'You have {tries} tries to win the game\n')
            
    return tries


def mixer(list1,list2):
    random.shuffle(list1)
    random.shuffle(list2)


def r1_position():
    r1_pos = 0
    guess_options = range(1,11)
    
    while r1_pos not in guess_options:
        try:
            r1_pos = int(input(f'Pick a position in ROW 1 to flip [1-10]: '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if r1_pos not in guess_options:
                print(f'Invalid Entry, Please enter a number between 1 and 10')
    return r1_pos-1


def r2_position():
    r2_pos = 0
    guess_options = range(1,11)
    
    while r2_pos not in guess_options:
        try:
            r2_pos = int(input(f'Pick a position in ROW 1 to flip [1-10]: '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if r2_pos not in guess_options:
                print(f'Invalid Entry, Please enter a number between 1 and 10')
    return r2_pos-1


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def answer(cheat,a,b):
    if cheat == True:
        print('This is the answer to the game board:')
        print(a)
        print(b, '\n')


if __name__ == "__main__":
    main()








