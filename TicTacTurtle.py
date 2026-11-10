import turtle
import json
#Init Constants and turtle objects
screen = turtle.Screen()
DIST = screen.canvheight/3
t = turtle.Turtle()
t.speed(10)
t.pensize(3)
t.color("blue")
t.hideturtle()
# Init lists
token = ["x"]
board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
         ]
ctrs_to_brd = {
(-1,1):(0,0), (0,1):(0,1), (1,1):(0,2),
(-1,0):(1,0), (0,0):(1,1), (1,0):(1,2),
(-1,-1):(2,0), (0,-1):(2,1), (1,-1):(2,2)
    }

########################## Scoring Functions ##########################
def write_scores(scores):
    with open("scores.json", mode = "w") as file:
        json.dump(scores, file)
        print("#"*20,"\nscores saved")
        
def read_scores():
    with open("scores.json", mode = "r") as file:
        scores = json.load(file)
        print("#"*20,"\nscores loaded")
        return scores
    
def restart_scores():
    scores = {"x":0,"o":0}
    write_scores(scores)

def print_high_scores():
    scores = read_scores()
    print("HIGH SCORES")
    print("#"*20)
    for token in ["x","o"]:
        print(f"{token} has {scores[token]} wins")
    print("#"*20)
#######################################################################

########################## Displaying the Board #######################

def update_board(x,y):
    x = x/DIST
    y = y/DIST
    row,collum = ctrs_to_brd[(x,y)]
    board[row][collum] = token[0]

def draw_board():
    lines = [(-0.5,1.5), (1.5,0.5), (0.5,-1.5), (-1.5,-0.5)]
    for x,y in lines:
        t.teleport(DIST*x,DIST*y)
        t.right(90)
        t.forward(DIST*3)


#######################################################################

########################## Drawing Tokens #############################
def find_center(x,y):  
    x /= DIST
    y /= DIST
    if x > 0.5:
        x = 1
    elif x < -0.5:
        x = -1
    else:
        x = 0 
    
    if y > 0.5:
        y = 1
    elif y < - 0.5:
        y = -1
    else:
        y = 0
    
    
    print(x*DIST,y*DIST)
    return x*DIST,y*DIST
   
   
   
def draw_token(x,y):
    x,y = find_center(x,y)
    update_board(x,y)
    t.teleport(x,y)
    if token == ["x"]:
        t.color("orange")
        t.pensize(8)
        t.setheading(45)
        t.forward(50)
        t.backward(100)
        t.teleport(x,y)
        t.setheading(-45)
        t.forward(50)
        t.backward(100)
    elif token == ["o"]:
        t.color("pink")
        t.dot(75)
        t.color("black")
        t.dot(60)
        
    winner = checks_for_winners(token[0])
    
    if winner != None:
        t.teleport(0,150)
        t.write(f"Game Over\n{winner} is the winner!!!",
                align="center", font=("Arial", 20, "bold"))

        scores = read_scores()
        scores[winner] += 1
        write_scores(scores)
    else:
        switch_token()


    
    

def switch_token():
    if token[0] == "x":
        token[0] = "o"
    else:
        token[0] = "x"
#######################################################################

############################# Game Loop ###############################
def checks_for_winners(token):
    
    for idx in range(3):
            # check rows
        if board[idx][0] == board[idx][1] == board[idx][2] == token:
            return token
            # check cols
        elif board[0][idx] == board[1][idx] == board[2][idx] == token:
            return token
        #check diags
    if board[0][0] == board[1][1] == board[2][2] == token:
        return token
    elif board[2][0] == board[1][1] == board[0][2] == token:
        return token

#######################################################################

################### Calling functions and stuff #########################
     
#winner = game_loop()
restart_scores()
print_high_scores()
# read in the scores and save as scores
###scores = read_scores()
# add one to the correct score
###scores[winner] += 1
# write the scores to the json file

# Commented these out for the game works in the terminal. 
screen.onclick(draw_token)
draw_board()
turtle.mainloop()

