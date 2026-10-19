player1Wins = 0
player2Wins = 0
totalPlayer1Wins = 0
totalPlayer2Wins = 0

import random

print("Hello, and welcome to Tic Tac To! what is Player 1's name?")
player1 = input()


print(f"Great to meet you {player1}!")
print("How many humans are competeing?")
gamemode = input().lower()

if gamemode == "2" or gamemode == "two":
     print("who is Player2? \n")
     player2 = input()
else:
    player2 = "CPU"
print(f"Great, now lets begin!")
print("You will Press the number key associated with your desired spot to play your turn")


play_again = True

while play_again:

    total_board = totalPlayer1Wins, totalPlayer2Wins

    print("The current score is ", total_board)


    player1Wins = 0
    player2Wins = 0


    while player1Wins < 2 and player2Wins < 2:

        scoreboard = player1Wins , player2Wins

        tictactoboard = [
            "[0]", "[1]", "[2]",
            "[3]", "[4]", "[5]",
            "[6]", "[7]", "[8]"
        ]

        winconditions = [
            [ 0, 1, 2 ],
            [ 3, 4, 5 ],
            [ 6, 7, 8 ],
            [ 0, 3, 6 ],
            [ 1, 4, 7 ],
            [ 2, 5, 8 ],
            [ 0, 4, 8 ],
            [ 2, 4, 6 ]
        ]

        def printBoard(tictacboard):
            print(tictacboard[0], tictacboard[1], tictacboard[2])
            print(tictacboard[3], tictacboard[4], tictacboard[5])
            print(tictacboard[6], tictacboard[7], tictacboard[8])





        winner = False

        token = "O"

        def checkwin(tictactoboard, token, winconditions):
            for i in range(8):
                if (tictactoboard[winconditions[i][0]] == token
                    and tictactoboard[winconditions[i][1]] == token
                    and tictactoboard[winconditions[i][2]] == token):

                    return True

            return False
            
            
        for turn in range(9):
            if token == "O":
                token = "X"
            else:
                token = "O"

            printBoard(tictactoboard)

            if gamemode != "2" or gamemode == "two" and token == "O":
                print("\n\n")
                availableCells = []

                for i in range(9):
                    if tictactoboard[i] != "O" and tictactoboard[i] != "X":
                        availableCells.append(i)

                cell = random.choice(availableCells)
            else:
                print("Choose a cell")
                cell = int(input())

            tictactoboard[cell] = token
            printBoard(tictactoboard)

            if checkwin(tictactoboard, token, winconditions):
                if token == "X":
                    player1Wins += 1
                    print(f" {player1} Wins!", print(f"\n {scoreboard}"))
                else:
                    player2Wins += 1
                    print(f"{player2} Wins!", print(f"\n {scoreboard}"))
                winner = True
                print(f"Score: {player1Wins} - {player2Wins}")
                break

    if not winner:
        print("Cat's Game! \n \n")
    totalPlayer1Wins += player1Wins
    totalPlayer2Wins += player2Wins
    print("Would you like to play again? (yes/no)")
    answer = input().lower()

    if answer == "no" or answer == "n" or answer == "No" or answer == "N" or answer == "Nah" or answer == "nah" or answer == "go to hell":
        play_again = False

print("The current score is ", total_board)
print("\n\n")

print(f"\n Thank you, \n  \tI hope you have enjoyed your time playing \n {player1} \n and \n {player2}\nHave a wonderful day!")
