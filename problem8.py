# Problem Description
"""
Your task is to create a game called guess the number.
Why is playing ? Computer vs Human. Computer has the role of
choosing a number from range specified by user. (User at the start
of the program chooses the range i.e. 0 - 100). After user chooses
a range he is greeted by a message saying something like "Welcome to,
this game blah blah...". Then the game may begin. Whole game is inside
of while loop that first asks a user for a number. (remember to convert
the input to int) and then computer decides whether the user guessed the
number or if its lower or higher. If user guesses he wins and there is
celebration message with congratulation to the winner.
"""
from random import randint
from rich import print

# Asking user the range
minRange = int(input("Enter the range min: "))
maxRange = int(input("Enter the range max: "))
playerLives = int(input("Enter the player lives: "))

# Computer generating number
compNum = randint(minRange, maxRange)

# Greeting message
print("Welcome to guess random number game")

gameOver = False


# The main loop
while True:
    # Asking number
    playerNumber = int(input("Enter the number: "))

    # Guess ?
    if playerNumber == compNum:
        break

    # Higher ?
    elif playerNumber < compNum:
        playerLives -= 1
        print("[red]Higher[/red]")
    # Lower ?
    elif playerNumber > compNum:
        playerLives -= 1
        print("[red]Lower[/red]")

    if playerLives == 0:
        gameOver = True
        break

# Celebration
if gameOver:
    print(f"[red]Game over[/red], you lost. The comp num was {compNum}")
else:
    print(f"[green]Congrats[/green], you won! Remaining lives {playerLives}")


# Can you do better ? 1
"""
Create a certain amount of lives for each user lets say 10. If the user misses the guess,
his lives will decrease by one. If there are no lives remaining he lost and a message game
over prints.
"""



# Can you do better ? 2
"""
Add nice color formatting to your program, try using rich instead of colorma library
"""

