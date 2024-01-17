import random


def main():

    # Settings
    ans = False         # Set ans to True to show the answer before playing
    debug = False       # Set debug to True to show the tries and remainder printed with the gameboard
    shuffle = True      # To shuffle the rows, set to False to use default board: For debugging

    # Initial Rows before shuffle -> Default board
    r1 = ['🍇','🍊','🍋','🍏','🍆','🍄','🥟','🌎','🧡','🐶']
    r2 = ['🍇','🍊','🍋','🍏','🍆','🍄','🥟','🌎','🧡','🐶']

    print("Welcome to Emoji Match\n")
    print("There are 10 'pictures' (emojis) in ROW 1, and similarly 10 idendical pictures in ROW 2")
    print("The ojective of the game is to match the PICTURES in ROW 1 to the PICTURES in ROW 2, which have been randomised")    

    while True:

        # Sets a counter to determine when the game has ended
        remainder = len(r1)

        # Creates a board with `~` as placeholders and prints it to begin the game
        board = list(range(1,11)) * 2
        print(game_board(board))
        print("\nLower tries = harder game. Test your luck!!!")

        # Ask the user how many attempts they want
        tries = attempts()
        
        # Shuffles the rows in place, shuffle parameter used to disable/enable function
        mixer(shuffle, r1, r2)

        # Displays the answer before the game begins,ans parameter used to disable/enable function: For debugging
        answer(ans, r1, r2)

        # Game code
        while tries > 0 and remainder !=0:
            
            
            guess_r1 = r1_position()
            guess_r2 = r2_position()

            if r1[guess_r1] == r2[guess_r2] or r2[guess_r2] == r1[guess_r1]:
                if board[guess_r1] == r1[guess_r1] or board[guess_r2] == r2[guess_r2]:
                    print(f'You have already matched {r1[guess_r1]}')
                else:
                    remainder = remainder - 1
                    print(f'\nCORRECT, Matched {r1[guess_r1]}\n')
                    print(f'There are {remainder} combinations left to match')

                    board[guess_r1] = r1[guess_r1]
                    board[guess_r2+10] = r2[guess_r2]

                    print(game_board(board))
                    if debug:
                        print(f"Tries: {tries}\nRemainder: {remainder}")
                
            else:
                tries = tries - 1
                print('\nNO MATCH', end="\t")
                if tries == 1:
                    print(f'(You have {tries} try left)')
                else:
                    print(f'(You have {tries} tries left)')

                print(game_board(board))
                if debug:
                    print(f"Tries: {tries}\nRemainder: {remainder}")

                if tries == 0:
                    print('\nGAME OVER')
                    print('You have ran out of tries\n')
                    answer(True, r1, r2)
                else:
                    print('\nHINT:')
                    print(f'\tROW 1 position {guess_r1+1} is {r1[guess_r1]}')
                    print(f'\tROW 2 position {guess_r2+1} is {r2[guess_r2]}\n')

            if remainder == 0:
                print('\n\nCONGRATULATIONS')
                print('You won\n')

        if not replay():
            break


# Functions used to control game below:
        
def game_board(board):
    """
    Function to print out the game board
    """
    b_str = f"\nROW 1 --- | {board[0]} | {board[1]} | {board[2]} | {board[3]} | {board[4]} | {board[5]} | {board[6]} | {board[7]} | {board[8]} | {board[9]} |" + \
    f"\n{"-"*50}|" + \
    f"\nROW 2 --- | {board[10]} | {board[11]} | {board[12]} | {board[13]} | {board[14]} | {board[15]} | {board[16]} | {board[17]} | {board[18]} | {board[19]} |"
    
    return b_str


def attempts():
    """
    Function to ask the user how many attempts they want
    Inclides error handling to catch incorrect user input
    """
    tries = 0
    options = range(1,21)
    
    while tries not in options:
        try:
            tries = int(input('How many tries would you like? [1-20] '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if tries < 0:
                print('Tries cannot be NEGATIVE!!')
            elif tries == 0:
                print('Tries cannot be ZERO')
        if tries not in options:
            print(f'Please enter a number between 1 and {options[-1]}')
            
    
    if tries in options:
        if tries == 1:
            print(f'You have {tries} try to win the game\n')
        else:
            print(f'You have {tries} tries to win the game\n')
            
    return tries


def mixer(shuffle, list1,list2):
    """
    Function to shuffle the rows in place
    """
    if shuffle:
        random.shuffle(list1)
        random.shuffle(list2)
    else:
        print("Mixer disabled, default board used\n")


def r1_position():
    """
    Function to get the users guess for row 1 position
    """

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
    """
    Function to get the users guess for row 2 position
    """

    r2_pos = 0
    guess_options = range(1,11)
    
    while r2_pos not in guess_options:
        try:
            r2_pos = int(input(f'Pick a position in ROW 2 to flip [1-10]: '))
        except ValueError:
            print('Must be a number. Try again!')
        else:
            if r2_pos not in guess_options:
                print(f'Invalid Entry, Please enter a number between 1 and 10')
    return r2_pos-1


def replay():
    """
    Function to ask the user if they wish to play again
    """
    again = input('Do you want to play again? Enter Yes or No: [Default: No] ').lower()
    if not again:
        return False
    while again not in ["yes", "no","y", "n"]:
        print('Invalid Entry')
        return False
    else:
        if again in ['y', 'yes']:
            return True
        else:
            return False
        

def answer(ans,a,b):
    """
    Function print the answer at the end of the game and for debugging
    """

    if ans == True:
        print('This is the answer to the game board:')
        print(a)
        print(b, '\n')


if __name__ == "__main__":
    main()








