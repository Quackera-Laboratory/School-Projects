import json

def write_scores(scores):
    with open("scores.json", mode = "w") as file:
        json.dump(scores, file)
        print("#"*20,"\nScores saved")
        
def read_scores():
    with open("scores.json", mode = "r") as file:
        scores = json.load(file)
        print("#"*20,"\nScores loaded")
        return scores
    
def restart_scores():
    scores = {"x":0,"o":0}
    write_scores(scores)
    
def print_high_scores():
    scores = read_scores()
    print("HIGH SCORES")
    print("#*20")
    for token in ["x","o"]:
        print(f"{token} has {scores[token]} wins")
    print("#*20")

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
def print_board():
#board[row][column]
    print(f' {board[0][0]} | {board[0][1]} | {board[0][2]} ')
    print('-----------')
    print(f' {board[1][0]} | {board[1][1]} | {board[1][2]} ')
    print('-----------')
    print(f' {board[2][0]} | {board[2][1]} | {board[2][2]} ')
def game_loop():
# initialize the token as x
    token = "x"
    for turn in range(9):
        print_board()
        move = int(input(f"Please put {token} somewhere"))
        for row in range(3):
            for col in range(3):
                if move == board[row][col]:
                    board[row][col] = token
        for idx in range(3):
        # check rows
            if board[idx][0]==board[idx][1]==board[idx][2]:
                print(f"{token} is the winner")
                return
# check cols
            elif board[0][idx]==board[1][idx]==board[2][idx]:
                print(f"{token} is the winner")
                return
            #check diags
            if board[0][0]==board[1][1]==board[2][2]:
                print(f"{token} is the winner")
                return
            elif board[2][0]==board[1][1]==board[0][2]:
                print(f"{token} is the winner")
                return
            if token == "x":
                token = "o"
            else:
                token = "x"
            
#################################################
              
winner = game_loop()


#read scores and save as scores
scores = read_scores()
#restart_scores()
#add one to the correct score
scores[winner] += 1
write_scores(scores)
#write the scores to the json file

#play the game to test