player1Wins = 0
player2Wins = 0

scoreboard = player1Wins , player2Wins

print("Hello, and welcome to Tic Tac To! what is Player 1's name?")
player1 = input()
print(f"Great to meet you {player1}, and who is Player2?")
player2 = input()
print(f"Great having you as well {player2}, now lets begin!")
print("You will Press the number key associated with your desired spot to play your turn")

while player1Wins < 2 and player2Wins < 2:

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
        
        #for (i = 4; i > 0;i)
    for turn in range(9):
        if token == "O":
            token = "X"
        else:
            token = "O"

        printBoard(tictactoboard)

        print("Choose a cell \n")
        cell = int(input())

        tictactoboard[cell] = token

        printBoard(tictactoboard)
        if checkwin(tictactoboard, token, winconditions):
            if token == "X":
                player1Wins += 1
                print(f" {player1} Wins!", print("\n {scoreboard}"))
            else:
                player2Wins += 1
                print(f"{player2} Wins!", print("\n {scoreboard}"))
            winner = True
            break
if not winner:
    print("Cat's Game!")