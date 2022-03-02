import random

rundNumber = 1
player = 0
computer = 0
while(rundNumber<=3):
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    computer_choice = random.randint(0, 2)
    print("ROUND " + str(rundNumber))
    if(player_choice==0):
        if(computer_choice==0):
            print("You choose ROCK, Computer choose ROCK, it's a draw")
        elif(computer_choice==1):
            print("You choose ROCK, Computer choose PAPER, you loose")
            computer+=1
        elif(computer_choice==2):
            print("You choose ROCK, Computer choose SCISSORS, you won")
            player+=1
    elif(player_choice==1):
        if(computer_choice==0):
            print("You choose PAPER, Computer choose ROCK, you won")
            player += 1
        elif(computer_choice==1):
            print("You choose PAPER, Computer choose PAPER, it's a draw")
        elif(computer_choice==2):
            print("You choose PAPER, Computer choose PAPER, you lose")
            computer += 1
    elif(player_choice==2):
        if(computer_choice==0):
            print("You choose SCISSORS, Computer choose ROCK, you lost")
            computer += 1
        elif(computer_choice==1):
            print("You choose SCISSORS, Computer choose PAPER, yow won")
            player += 1
        elif(computer_choice==2):
            print("You choose SCISSORS, Computer choose SCISSORS, it's a draw")

    rundNumber+=1
    print(f"RESULT COMP:{computer} PLAYER: {player}")
    print(f"To the end: {4-rundNumber}")

if(player>computer):
    print("YOU WIN")
else:
    print("COMPUTER WIN")
