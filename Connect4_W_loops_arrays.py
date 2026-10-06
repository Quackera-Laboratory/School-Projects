player1Wins = 0
player2Wins = 0

scoreboard = player1Wins , player2Wins


winner = False
token = "(-O)"


print("Hello, and welcome to Connect 4! what is Player 1's name?")
player1 = input()
print(f"Great to meet you {player1}, and who is Player2?")
player2 = input()
print(f"Great having you as well {player2}, now lets begin!")
print("You will Press the number key associated with your desired collum to play your turn")



while player1Wins < 2 and player2Wins < 2:

    print_board = [
        "[0] ", "[1]", " [2] ", "[3] ", "[4]", "[5] ", " [6] ",
        "[7] ", "[8] ", "[9] ", "[10]", "[11]", "[12]", "[13]",
        "[14]", "[15]", "[16]", "[17]", "[18]", "[19]", "[20]",
        "[21]", "[22]", "[23]", "[24]", "[25]", "[26]", "[27]",
        "[28]", "[29]", "[30]", "[31]", "[32]", "[33]", "[34]",
        "[35]", "[36]", "[37]", "[38]", "[39]", "[40]", "[41]"
    ]
    def printboard(print_board):
            print(print_board[0], print_board[1], print_board[2], print_board[3], print_board[4], print_board[5], print_board[6])
            print(print_board[7], print_board[8], print_board[9], print_board[10], print_board[11], print_board[12], print_board[13])
            print(print_board[14], print_board[15], print_board[16], print_board[17], print_board[18], print_board[19], print_board[20])
            print(print_board[21], print_board[22], print_board[23], print_board[24], print_board[25], print_board[26], print_board[27])
            print(print_board[28], print_board[29], print_board[30], print_board[31], print_board[32], print_board[33], print_board[34])
            print(print_board[35], print_board[36], print_board[37], print_board[38], print_board[39], print_board[40], print_board[41])
    
    for turn in range(42):
        if token == "(-O)":
            token = "(-X)"
        else:
            token = "(-O)"

        printboard(print_board)
        
        print("Choose a slot, slots are chosen with numbers 0, 1, 2, 3, 4, 5, 6, \n")
        slot = int(input("slot: "))
        for row in range(5, -1, -1):
            position = slot + (row * 7)

            if print_board[position] == f"[{position}]":
                print_board[position] = token
                break
        
        


