# EMOJI MATCH

Welcome to Emoji Match, a simple console-based game where your objective is to match pairs of emojis. This game is built in Python and utilizes basic console input/output for interaction.

## How to Play
1. Run the program in a Python environment.
2. Follow the on-screen instructions to play the game.
3. The game presents two rows of emojis initially, both identical. Your goal is to match the emojis in the first row with their corresponding positions in the second row after they have been shuffled randomly.
4. You have a limited number of attempts to find all the matches.

#### Video Demo:  https://www.youtube.com/watch?v=reELDq0xZcs

#### Description:
Emoji match is a python spin-off of a popular childrens memory card game, where a player flips over 2 cards to attempt to match the cards. If the 2 cards are matched correctly then the card remain right-side-up. If the 2 chosen cards to not match, the cards are flipped back over so it is hidden and the player needs to remember what card is placed where in an attempt to uncover all the cards to win the game.

The original (physical) card game has no limit on card flip attempts, but in Emoji Match there is a limted amount of attempts. This adds a level of difficulty to the game. The game difficulty is inversely proportional to the number of attempts chosen by the player.

After the players chooses the number of tries they will like, the game will then prompt the user to flip a card from row 1 and row 2 respectively. If there is a match, the player will be notified and the correct images will be printed on a "game board" to visually depict the players answer. If there is no match, there game will print the current "game board" and give the player a hint of what emojis are located in the chosen spots. The number of tries is reduced by 1 and the player chooses again. This is repeated until the player runs of of tries or wins the game. If the player fails to match all the tiles and runs out of tries, the game will print out the solution. Thereafter the player is asked if they wish to play again. An `Y or YES` input is required to play again, any other input will exit the game.

##### Debugging options
- Set `ans` to `True` to display the answer before playing for debugging purposes.
- Set `debug` to `True` to show the number of tries and remainder on the game board.
- Set `shuffle` to `True` to shuffle the rows at the beginning of each game. Set it to `False` to use the default board for debugging.
