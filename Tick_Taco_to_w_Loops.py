a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9

def print_board():
    print(f' {a}| {b}  |  {c}')
    print('-------------')
    print(f' {d}| {e}  |  {f}')
    print('-------------')
    print(f' {g}| {h}  |  {i}')

for loop in range(5):
    print_board()


    
    token = "X"

    print_board()
    move = int(input('move'))
    if move == 1:
        if a == 1:
            a = token
        else:
            print("\n point already plotted")

    elif move == 2:
        if b == 2:
            b = token
        else:
            print(" \n point already ploted")
    elif move == 3:
        if c == 3:
            c = token
        else:
            print(" \n point already ploted")
    elif move == 4:
        if d == 4:
            d = token
        else:
            print(" \n point already ploted")
    elif move == 5:
        if e == 5:
            e = token
        else:
            print("\n point already ploted")
    elif move == 6:
        if f == 6:
            f = token
        else:
            print("\n point already ploted")
    elif move == 7:
        if g == 7:
            g = token
        else:
            print("\n point already ploted")
    elif move == 8:
        if h == 8:
            h = token
        else:
            print("\n point already ploted")
    elif move == 9:
        if i == 9:
            i = token
        else:
            print("\n point already ploted")

    if a == token and b == token and c == token:
        print({token}, "wins!")
        quit()
    if a == token and d == token and g == token:
        print({token}, "wins!")
        quit()
    if a == token and e == token and i == token:
        print({token}, "wins!")
        quit()
    if b == token and e == token and h == token:
        print({token}, "wins!")
        quit()
    if d == token and e == token and f == token:
        print({token}, "wins!")
        quit()
    if g == token and h == token and i == token:
        print({token}, "wins!")
        quit()
    if g == token and e == token and c == token:
        print({token}, "wins!")
        quit()
    if c == token and f == token and i == token:
        print({token}, "wins!")
        quit()
    
    token = "O"
    print_board()
    move = int(input('move'))
    if move == 1:
        if a == 1:
            a = token
        else:
            print("\n point already plotted")

    elif move == 2:
        if b == 2:
            b = token
        else:
            print(" \n point already ploted")
    elif move == 3:
        if c == 3:
            c = token
        else:
            print(" \n point already ploted")
    elif move == 4:
        if d == 4:
            d = token
        else:
            print(" \n point already ploted")
    elif move == 5:
        if e == 5:
            e = token
        else:
            print("\n point already ploted")
    elif move == 6:
        if f == 6:
            f = token
        else:
            print("\n point already ploted")
    elif move == 7:
        if g == 7:
            g = token
        else:
            print("\n point already ploted")
    elif move == 8:
        if h == 8:
            h = token
        else:
            print("\n point already ploted")
    elif move == 9:
        if i == 9:
            i = token
        else:
            print("\n point already ploted")
    
    if a == token and b == token and c == token:
        print({token}, "wins!")
        quit()
    if a == token and d == token and g == token:
        print({token}, "wins!")
        quit()
    if a == token and e == token and i == token:
        print({token}, "wins!")
        quit()
    if b == token and e == token and h == token:
        print({token}, "wins!")
        quit()
    if d == token and e == token and f == token:
        print({token}, "wins!")
        quit()
    if g == token and h == token and i == token:
        print({token}, "wins!")
        quit()
    if g == token and e == token and c == token:
        print({token}, "wins!")
        quit()
    if c == token and f == token and i == token:
        print({token}, "wins!")
        quit()
        
print_board()
    
print("Cat's Game!")
quit()
    