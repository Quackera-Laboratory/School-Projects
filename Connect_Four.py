a1 = 11
a2 = 12
a3 = 13
a4 = 14
a5 = 15
a6 = 16

b1 = 21
b2 = 22
b3 = 23
b4 = 24
b5 = 25
b6 = 26

c1 = 31
c2 = 32
c3 = 33
c4 = 34
c5 = 35
c6 = 36

d1 = 41
d2 = 42
d3 = 43
d4 = 44
d5 = 45
d6 = 46

e1 = 51
e2 = 52
e3 = 53
e4 = 54
e5 = 55
e6 = 56

f1 = 61
f2 = 62
f3 = 63
f4 = 64
f5 = 65
f6 = 66

g1 = 71
g2 = 72
g3 = 73
g4 = 74
g5 = 75
g6 = 76

def check_win():
    # Horizontal wins

    if a1 == token and b1 == token and c1 == token and d1 == token:
        print(token, "wins!")
        quit()

    if b1 == token and c1 == token and d1 == token and e1 == token:
        print(token, "wins!")
        quit()

    if c1 == token and d1 == token and e1 == token and f1 == token:
        print(token, "wins!")
        quit()

    if d1 == token and e1 == token and f1 == token and g1 == token:
        print(token, "wins!")
        quit()


    if a2 == token and b2 == token and c2 == token and d2 == token:
        print(token, "wins!")
        quit()

    if b2 == token and c2 == token and d2 == token and e2 == token:
        print(token, "wins!")
        quit()

    if c2 == token and d2 == token and e2 == token and f2 == token:
        print(token, "wins!")
        quit()

    if d2 == token and e2 == token and f2 == token and g2 == token:
        print(token, "wins!")
        quit()


    if a3 == token and b3 == token and c3 == token and d3 == token:
        print(token, "wins!")
        quit()

    if b3 == token and c3 == token and d3 == token and e3 == token:
        print(token, "wins!")
        quit()

    if c3 == token and d3 == token and e3 == token and f3 == token:
        print(token, "wins!")
        quit()

    if d3 == token and e3 == token and f3 == token and g3 == token:
        print(token, "wins!")
        quit()


    if a4 == token and b4 == token and c4 == token and d4 == token:
        print(token, "wins!")
        quit()

    if b4 == token and c4 == token and d4 == token and e4 == token:
        print(token, "wins!")
        quit()

    if c4 == token and d4 == token and e4 == token and f4 == token:
        print(token, "wins!")
        quit()

    if d4 == token and e4 == token and f4 == token and g4 == token:
        print(token, "wins!")
        quit()


    if a5 == token and b5 == token and c5 == token and d5 == token:
        print(token, "wins!")
        quit()

    if b5 == token and c5 == token and d5 == token and e5 == token:
        print(token, "wins!")
        quit()

    if c5 == token and d5 == token and e5 == token and f5 == token:
        print(token, "wins!")
        quit()

    if d5 == token and e5 == token and f5 == token and g5 == token:
        print(token, "wins!")
        quit()


    if a6 == token and b6 == token and c6 == token and d6 == token:
        print(token, "wins!")
        quit()

    if b6 == token and c6 == token and d6 == token and e6 == token:
        print(token, "wins!")
        quit()

    if c6 == token and d6 == token and e6 == token and f6 == token:
        print(token, "wins!")
        quit()

    if d6 == token and e6 == token and f6 == token and g6 == token:
        print(token, "wins!")
        quit()


    # Vertical wins

    if a1 == token and a2 == token and a3 == token and a4 == token:
        print(token, "wins!")
        quit()

    if a2 == token and a3 == token and a4 == token and a5 == token:
        print(token, "wins!")
        quit()

    if a3 == token and a4 == token and a5 == token and a6 == token:
        print(token, "wins!")
        quit()


    if b1 == token and b2 == token and b3 == token and b4 == token:
        print(token, "wins!")
        quit()

    if b2 == token and b3 == token and b4 == token and b5 == token:
        print(token, "wins!")
        quit()

    if b3 == token and b4 == token and b5 == token and b6 == token:
        print(token, "wins!")
        quit()


    if c1 == token and c2 == token and c3 == token and c4 == token:
        print(token, "wins!")
        quit()

    if c2 == token and c3 == token and c4 == token and c5 == token:
        print(token, "wins!")
        quit()

    if c3 == token and c4 == token and c5 == token and c6 == token:
        print(token, "wins!")
        quit()


    if d1 == token and d2 == token and d3 == token and d4 == token:
        print(token, "wins!")
        quit()

    if d2 == token and d3 == token and d4 == token and d5 == token:
        print(token, "wins!")
        quit()

    if d3 == token and d4 == token and d5 == token and d6 == token:
        print(token, "wins!")
        quit()


    if e1 == token and e2 == token and e3 == token and e4 == token:
        print(token, "wins!")
        quit()

    if e2 == token and e3 == token and e4 == token and e5 == token:
        print(token, "wins!")
        quit()

    if e3 == token and e4 == token and e5 == token and e6 == token:
        print(token, "wins!")
        quit()


    if f1 == token and f2 == token and f3 == token and f4 == token:
        print(token, "wins!")
        quit()

    if f2 == token and f3 == token and f4 == token and f5 == token:
        print(token, "wins!")
        quit()

    if f3 == token and f4 == token and f5 == token and f6 == token:
        print(token, "wins!")
        quit()


    if g1 == token and g2 == token and g3 == token and g4 == token:
        print(token, "wins!")
        quit()

    if g2 == token and g3 == token and g4 == token and g5 == token:
        print(token, "wins!")
        quit()

    if g3 == token and g4 == token and g5 == token and g6 == token:
        print(token, "wins!")
        quit()


    # Diagonal wins - bottom left to top right

    if a1 == token and b2 == token and c3 == token and d4 == token:
        print(token, "wins!")
        quit()

    if b1 == token and c2 == token and d3 == token and e4 == token:
        print(token, "wins!")
        quit()

    if c1 == token and d2 == token and e3 == token and f4 == token:
        print(token, "wins!")
        quit()

    if d1 == token and e2 == token and f3 == token and g4 == token:
        print(token, "wins!")
        quit()

    if a2 == token and b3 == token and c4 == token and d5 == token:
        print(token, "wins!")
        quit()

    if b2 == token and c3 == token and d4 == token and e5 == token:
        print(token, "wins!")
        quit()

    if c2 == token and d3 == token and e4 == token and f5 == token:
        print(token, "wins!")
        quit()

    if d2 == token and e3 == token and f4 == token and g5 == token:
        print(token, "wins!")
        quit()

    if a3 == token and b4 == token and c5 == token and d6 == token:
        print(token, "wins!")
        quit()

    if b3 == token and c4 == token and d5 == token and e6 == token:
        print(token, "wins!")
        quit()

    if c3 == token and d4 == token and e5 == token and f6 == token:
        print(token, "wins!")
        quit()

    if d3 == token and e4 == token and f5 == token and g6 == token:
        print(token, "wins!")
        quit()


    # Diagonal wins - top left to bottom right

    if a4 == token and b3 == token and c2 == token and d1 == token:
        print(token, "wins!")
        quit()

    if b4 == token and c3 == token and d2 == token and e1 == token:
        print(token, "wins!")
        quit()

    if c4 == token and d3 == token and e2 == token and f1 == token:
        print(token, "wins!")
        quit()

    if d4 == token and e3 == token and f2 == token and g1 == token:
        print(token, "wins!")
        quit()

    if a5 == token and b4 == token and c3 == token and d2 == token:
        print(token, "wins!")
        quit()

    if b5 == token and c4 == token and d3 == token and e2 == token:
        print(token, "wins!")
        quit()

    if c5 == token and d4 == token and e3 == token and f2 == token:
        print(token, "wins!")
        quit()

    if d5 == token and e4 == token and f3 == token and g2 == token:
        print(token, "wins!")
        quit()

    if a6 == token and b5 == token and c4 == token and d3 == token:
        print(token, "wins!")
        quit()

    if b6 == token and c5 == token and d4 == token and e3 == token:
        print(token, "wins!")
        quit()

    if c6 == token and d5 == token and e4 == token and f3 == token:
        print(token, "wins!")
        quit()

    if d6 == token and e5 == token and f4 == token and g3 == token:
        print(token, "wins!")
        quit()

token = 'O'
def print_board():
    print(f'|_{a1}_|_{b1}_||_{c1}_|_{d1}_||_{e1}_|_{f1}_||_{g1}_|')
    print(f'|_{a2}_|_{b2}_||_{c2}_|_{d2}_||_{e2}_|_{f2}_||_{g2}_|')
    print(f'|_{a3}_|_{b3}_||_{c3}_|_{d3}_||_{e3}_|_{f3}_||_{g3}_|')
    print(f'|_{a4}_|_{b4}_||_{c4}_|_{d4}_||_{e4}_|_{f4}_||_{g4}_|')
    print(f'|_{a5}_|_{b5}_||_{c5}_|_{d5}_||_{e5}_|_{f5}_||_{g5}_|')
    print(f'|_{a6}_|_{b6}_||_{c6}_|_{d6}_||_{e6}_|_{f6}_||_{g6}_|')
    
print_board()

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')

else:
    print('Invalid column')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
    print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
print_board()

check_win()

token = 'B2'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
        
print_board()

check_win()

token = 'O'

move = input('Choose a column: ')

if move == '1':
    if a6 == 16:
        a6 = token
    elif a5 == 15:
        a5 = token
    elif a4 == 14:
        a4 = token
    elif a3 == 13:
        a3 = token
    elif a2 == 12:
        a2 = token
    elif a1 == 11:
        a1 = token
    else:
        print('Column is full')

elif move == '2':
    if b6 == 26:
        b6 = token
    elif b5 == 25:
        b5 = token
    elif b4 == 24:
        b4 = token
    elif b3 == 23:
        b3 = token
    elif b2 == 22:
        b2 = token
    elif b1 == 21:
        b1 = token
    else:
        print('Column is full')

elif move == '3':
    if c6 == 36:
        c6 = token
    elif c5 == 35:
        c5 = token
    elif c4 == 34:
        c4 = token
    elif c3 == 33:
        c3 = token
    elif c2 == 32:
        c2 = token
    elif c1 == 31:
        c1 = token
    else:
        print('Column is full')

elif move == '4':
    if d6 == 46:
        d6 = token
    elif d5 == 45:
        d5 = token
    elif d4 == 44:
        d4 = token
    elif d3 == 43:
        d3 = token
    elif d2 == 42:
        d2 = token
    elif d1 == 41:
        d1 = token
    else:
        print('Column is full')

elif move == '5':
    if e6 == 56:
        e6 = token
    elif e5 == 55:
        e5 = token
    elif e4 == 54:
        e4 = token
    elif e3 == 53:
        e3 = token
    elif e2 == 52:
        e2 = token
    elif e1 == 51:
        e1 = token
    else:
        print('Column is full')

elif move == '6':
    if f6 == 66:
        f6 = token
    elif f5 == 65:
        f5 = token
    elif f4 == 64:
        f4 = token
    elif f3 == 63:
        f3 = token
    elif f2 == 62:
        f2 = token
    elif f1 == 61:
        f1 = token
    else:
        print('Column is full')

elif move == '7':
    if g6 == 76:
        g6 = token
    elif g5 == 75:
        g5 = token
    elif g4 == 74:
        g4 = token
    elif g3 == 73:
        g3 = token
    elif g2 == 72:
        g2 = token
    elif g1 == 71:
        g1 = token
    else:
        print('Column is full')
