from random import randint

# save the player as a variable called player
# the value of player will be one of three choices to type (input)
# Boolean values are true or False - you can use these to check # state and then make programming choices based on their value
player = False

# an array is just a container. It holds multiple values in a
#  0-based index
# you can store anything in an array, and retrieve it later. Arrays have square bracket notation
choices = ["rock", "paper", "scissors"]

# add player and computer lives
playerLives = 2
computerLives = 2

# define a win/lose function and invoke it in our gaame loop when lives run out (player or computer)

def winorlose(status):
    print("You " + status + "! would you like to play again?")
    choice = input(" Y / N ")

    global playerLives
    global computerLives
    global player

    if choice == "n":
        print("See you soon!")
        exit()
    else:
        #reset and restart the game 
         playerLives = 2
         computerLives = 2
         player = False
            
# create an infinite loop (for now) so that we can keep playing 

while player is False:
    player = input("Choose your weapon: rock, paper or scissors: ")
    computer = choices[randint(0, 2)]

    print("player chose: " + player)
    print("computer chose: " + computer)

    if computer == player:
        print("tie! try again")

    elif player == "rock":
        if computer == "paper":
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    elif player == "paper":
        if computer == "scissors":
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    elif player == "scissors":
        if computer == "rock":
            print("you lose!")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    print("player Lives: " + str(playerLives))
    print("computer Lives: " + str(computerLives))

    if playerLives == 0:
        # call the winorlose function here
        winorlose("lose")
        
    elif computerLives == 0:
        # call the winorlose function here  
        winorlose("won")   
        
    player = False
