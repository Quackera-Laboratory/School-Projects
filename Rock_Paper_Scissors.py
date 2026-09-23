rock = 1
scissors = 3
paper = 2
Rock = 1
Scissors = 3
Paper = 2

print('Hello,\n \t Welcome, \n \t \t Legendary Challengers!!!')

for loop in range(3):
    print("\n \n Choose your Weapons!!!")

##players 1 and 2 are input values to track independant

    player1 = (input('"Rock,\t Paper,\t Scissors!! \n'))
    if player1 == 'rock' or player1 == "Rock" or player1 == 'r' or player1 =="R":
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    
    elif player1 == 'paper' or player1 == 'Paper' or player1 == 'p' or player1 == "P":
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    elif player1 == 'scissors' or player1 == 'Scissors' or player1 == 's' or player1 == "S":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    player2 = (input('"Rock,\t Paper,\t Scissors!! \n'))
    if player2 == 'rock' or player2 == "Rock" or player2 == 'r' or player2 == "R":
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    
    elif player2 == 'Paper' or player2 == "Paper" or player2 == 'p' or player2 == "P":
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    elif player2 == 'scissors' or player2 == 'Scissors' or player2 == 's' or player2 == "S":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
##compare all 9 possible game states
    
    if (player1 == 'rock' or player1 == "Rock" or player1 == 'r' or player1 == "R") and (player2 == 'rock' or player2 == 'Rock' or player2 == 'r' or player2 == "R"):
        print('\n Two immortal dragons clash forever')

    elif (player1 == 'rock' or player1 == "Rock" or player1 == 'r' or player1 == "R") and (player2 == 'Paper' or player2 == "Paper" or player2 == 'p' or player2 == "P"):
        print('\n The rock crushed and pasted into a beautiful dress for the paper')
    
    elif (player1 == 'rock' or player1 == "Rock" or player1 == 'r' or player1 =="R") and (player2 == 'Scissors' or player2 == 'scissors' or player2 == 's' or player2 == "S"):
        print("\n The puny scissors clatter as seperated blades")
    
    elif (player1 == 'Paper' or player1 == 'paper' or player1 == 'p' or player1 == "P") and (player2 == "Paper" or player2 == "paper" or player2 == 'p' or player2 == "P"):
        print('\n Good luck cheating off each other now')
    
    elif (player1 == 'Paper' or player1 == 'paper' or player1 == 'p' or player1 == "p") and (player2 == 'Rocks' or player2 == 'rock'or player2 == 'r' or player2 == "R"):
        print('\n Poor Rock turned sedimantary')
    
    elif (player1 == 'Paper' or player1 == 'paper' or player1 == 'p' or player1 == "P") and (player2 == 'Scissors' or player2 == "scissors" or player2 == 's' or player2 == "S"):
        print('\n The paper made for a beautiful snow')
    
    elif (player1 == 'Scissors' or player1 == 'scissors' or player1 == 's' or player1 == "S") and (player2 == "Paper" or player2 == 'paper' or player2 == 'p' or player2 == "P"):
        print('\nTo Shreds you say?.')

    elif (player1 == 'Scissors' or player1 == 'scissors' or player1 == 's' or player1 == "S") and (player2 == "Scissors" or player2 == 'scissors' or player2 == 's' or player2 == "S"):
        print('\n the blades unsure of their absolute value each left.')
    elif (player1 == 'scissors' or player1 == "Scissors" or player1 == 's' or player1 == "S") and (player2 == 'rock' or player2 == "Rock" or player2 == 'r' or player2 == "R"):
        print('Hard Rock crushes thin steel')
    
