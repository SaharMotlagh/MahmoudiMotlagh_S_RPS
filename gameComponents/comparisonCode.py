from gameComponents import player, computer, playerLives, computerLives 


def player(status):
    print("player " + status)

def computer(status):    
    print("computer " + status)

def playerLives(status): 
    print("player Lives " + " status " + " player Lives: " + str(playerLives)")

def computerLives(status):    
    print("computer Lives " + " status " + " computer Lives: " + str(computerLives)")     

    if computer == player:
            print("+++++++++++++++++++++++++++++++++++")
            print("tie! try again")
            print("+++++++++++++++++++++++++++++++++++")

        elif player == "rock":
            if computer == "paper":
                print("^-^====^-^====^-^====^-^====^-^====^-^")
                print("you lose!")
                ("^-^====^-^====^-^====^-^====^-^====^-^")
                playerLives = playerLives - 1
            else:
                print("*-*==*-*==*-*==*-*==*-*==*-*==*-*")
                print("you win!")
                print("*-*==*-*==*-*==*-*==*-*==*-*==*-*")
                computerLives = computerLives - 1

        elif player == "paper":
            if computer == "scissors":
                print("^-^====^-^====^-^====^-^====^-^====^-^")
                print("you lose!")
                ("^-^====^-^====^-^====^-^====^-^====^-^")
                playerLives = playerLives - 1
            else:
                print("*-*====*-*====*-*====*-*====*-*====*-*")
                print("you win!")
                print("*-*==*-*==*-*==*-*==*-*==*-*==*-*")
                computerLives = computerLives - 1

        elif player == "scissors":
            if computer == "rock":
                print("^-^====^-^====^-^====^-^====^-^====^-^")
                print("you lose!")
                ("^-^====^-^====^-^====^-^====^-^====^-^")
                playerLives = playerLives - 1
            else:
                print("*-*====*-*====*-*====*-*====*-*====*-*")
                print("you win!")
                print("*-*==*-*==*-*==*-*==*-*==*-*==*-*")
                computerLives = computerLives - 1