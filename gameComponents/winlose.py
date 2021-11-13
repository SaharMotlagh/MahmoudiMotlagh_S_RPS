def winorlose(status):
    print("You " + status + "! would you like to play again?")
    choice = input(" Y / N ")

    global playerLives
    global computerLives
    global player

    if choice == "n":
        print("============See you soon!============")
        exit()
    else:
        #reset and restart the game 
         playerLives = 2
         computerLives = 2
         player = False