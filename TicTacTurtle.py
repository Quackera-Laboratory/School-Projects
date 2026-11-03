import turtle

screen = turtle.Screen()

centers = [
    (-1,1),(0,1),(1,1),
    (-1,0),(0,0),(1,0),
    (-1,-1),(0,-1),(1,-1)
    ]

DIST = screen.canvheight/3

t2 = turtle.Turtle()
t2.speed(80)
t2.color("blue")
#t2.hideturtle()

def draw_board():
    lines = [(-0.5,1.5), (1.5,0.5), (0.5,-1.5), (-1.5,-0.5)]
    for x,y in lines:
        t2.teleport(DIST*x,DIST*y)
        t2.right(90)
        t2.forward(DIST*3)

def draw_centers():
    for x,y in centers:
        t2.teleport(DIST*x, DIST*y)
        t2.dot(10,"black")
def find_center (x,y):
    
    x/=DIST
    y/=DIST
    
    if x > 0.5:
        x = 1
    elif x < - 0.5:
        x = -1
    else:
        x = 0
    
    if y > 0.5:
        y = 1
    elif y < - 0.5:
        y = -1
    else:
        y = 0 
    

    if y > 0.5*DIST:
        print("upper right")
    elif y <-0.5*DIST:
        print("lower right")
    else:
        print("middle")
        
    print(x*DIST, y*DIST)
    return(x*DIST, y*DIST)
             
# Make the conditionals for the rest of the cells do it first
    # without a loop, then add the loop if you want.
    
    return 

########################### TODO 2 #############################   
def draw_token(x,y):
    x,y = find_center(x,y)
    # Move the turtle to the center found in find_center()
    
    # Draw x or o
    t2.teleport(x,y)
    t2.setheading(45)
    t2.forward(50)
    t2.backward(100)
    t2.teleport(x,y)
    t2.setheading(-45)
    t2.forward(50)
    t2.backward(100)
########################### TODO 3 #############################
    
def switch_token():
    # We have to be able to alternate between x and o.
    # Try to make that happen here.
    pass
 
screen.onclick(draw_token)

draw_board()
draw_centers()
turtle.done()

 
