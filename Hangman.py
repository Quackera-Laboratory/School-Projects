#Hangman game

print('Hello, welcome to hangman')

#desighn board to be printed

def print_board():
    print("_ _ _ _ _")
    print("|       _")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("| _{}_{}_{}_{}_{}_{}_{}_{}_")
    
print_board()

#format selection of board depending on number of letters in completion word.