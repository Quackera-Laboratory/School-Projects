
a1 = 11
a2 = 12
a3 = 13
a4 = 14
a5 = 15
a6 = 16
a7 = 17
a8 = 18
a9 = 19
a10 = 10

b1 = 21
b2 = 22
b3 = 23
b4 = 24
b5 = 25
b6 = 26
b7 = 27
b8 = 28
b9 = 29
b10 = 20

c1 = 31
c2 = 32
c3 = 33
c4 = 34
c5 = 35
c6 = 36
c7 = 37
c8 = 38
c9 = 39
c10 = 30

d1 = 41
d2 = 42
d3 = 43
d4 = 44
d5 = 45
d6 = 46
d7 = 47
d8 = 48
d9 = 49
d10 = 40

e1 = 51
e2 = 52
e3 = 53
e4 = 54
e5 = 55
e6 = 56
e7 = 57
e8 = 58
e9 = 59
e10 = 50

f1 = 61
f2 = 62
f3 = 63
f4 = 64
f5 = 65
f6 = 66
f7 = 67
f8 = 68
f9 = 69
f10 = 60

g1 = 71
g2 = 72
g3 = 73
g4 = 74
g5 = 75
g6 = 76
g7 = 77
g8 = 78
g9 = 79
g10 = 70

h1 = 81
h2 = 82
h3 = 83
h4 = 84
h5 = 85
h6 = 86
h7 = 87
h8 = 88
h9 = 89
h10 = 80

i1 = 91
i2 = 92
i3 = 93
i4 = 94
i5 = 95
i6 = 96
i7 = 97
i8 = 98
i9 = 99
i10 = 90

j1 = 101
j2 = 102
j3 = 103
j4 = 104
j5 = 105
j6 = 106
j7 = 107
j8 = 108
j9 = 109
j10 = 100


#ship types
Carrier = 5
Battleship = 4
Submarine = 3
Cruiser = 3
Destroyer = 2

token = 'S'

# Create the two boards each player will use

def print_board1():
    print(f'{a1}  {b1}  {c1}  {d1}  {e1}  {f1}  {g1}  {h1}  {i1}  {j1}')
    print(f'{a2}  {b2}  {c2}  {d2}  {e2}  {f2}  {g2}  {h2}  {i2}  {j2}')
    print(f'{a3}  {b3}  {c3}  {d3}  {e3}  {f3}  {g3}  {h3}  {i3}  {j3}')
    print(f'{a4}  {b4}  {c4}  {d4}  {e4}  {f4}  {g4}  {h4}  {i4}  {j4}')
    print(f'{a5}  {b5}  {c5}  {d5}  {e5}  {f5}  {g5}  {h5}  {i5}  {j5}')
    print(f'{a6}  {b6}  {c6}  {d6}  {e6}  {f6}  {g6}  {h6}  {i6}  {j6}')
    print(f'{a7}  {b7}  {c7}  {d7}  {e7}  {f7}  {g7}  {h7}  {i7}  {j7}')
    print(f'{a8}  {b8}  {c8}  {d8}  {e8}  {f8}  {g8}  {h8}  {i8}  {j8}')
    print(f'{a9}  {b9}  {c9}  {d9}  {e9}  {f9}  {g9}  {h9}  {i9}  {j9}')
    print(f'{a10} {b10}  {c10}  {d10}  {e10}  {f10}  {g10}  {h10}  {i10}  {j10}')

print_board1()

def place_fire():
    global a1, a2, a3, a4, a5, a6, a7, a8, a9, a10
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10
    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10
    global d1, d2, d3, d4, d5, d6, d7, d8, d9, d10
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10
    global f1, f2, f3, f4, f5, f6, f7, f8, f9, f10
    global g1, g2, g3, g4, g5, g6, g7, g8, g9, g10
    global h1, h2, h3, h4, h5, h6, h7, h8, h9, h10
    global i1, i2, i3, i4, i5, i6, i7, i8, i9, i10
    global j1, j2, j3, j4, j5, j6, j7, j8, j9, j10

    place = int(input('Place ship: '))

    if place == 11:
        a1 = token
    elif place == 12:
        a2 = token
    elif place == 13:
        a3 = token
    elif place == 14:
        a4 = token
    elif place == 15:
        a5 = token
    elif place == 16:
        a6 = token
    elif place == 17:
        a7 = token
    elif place == 18:
        a8 = token
    elif place == 19:
        a9 = token
    elif place == 10:
        a10 = token

    elif place == 21:
        b1 = token
    elif place == 22:
        b2 = token
    elif place == 23:
        b3 = token
    elif place == 24:
        b4 = token
    elif place == 25:
        b5 = token
    elif place == 26:
        b6 = token
    elif place == 27:
        b7 = token
    elif place == 28:
        b8 = token
    elif place == 29:
        b9 = token
    elif place == 20:
        b10 = token

    elif place == 31:
        c1 = token
    elif place == 32:
        c2 = token
    elif place == 33:
        c3 = token
    elif place == 34:
        c4 = token
    elif place == 35:
        c5 = token
    elif place == 36:
        c6 = token
    elif place == 37:
        c7 = token
    elif place == 38:
        c8 = token
    elif place == 39:
        c9 = token
    elif place == 30:
        c10 = token

    elif place == 41:
        d1 = token
    elif place == 42:
        d2 = token
    elif place == 43:
        d3 = token
    elif place == 44:
        d4 = token
    elif place == 45:
        d5 = token
    elif place == 46:
        d6 = token
    elif place == 47:
        d7 = token
    elif place == 48:
        d8 = token
    elif place == 49:
        d9 = token
    elif place == 40:
        d10 = token

    elif place == 51:
        e1 = token
    elif place == 52:
        e2 = token
    elif place == 53:
        e3 = token
    elif place == 54:
        e4 = token
    elif place == 55:
        e5 = token
    elif place == 56:
        e6 = token
    elif place == 57:
        e7 = token
    elif place == 58:
        e8 = token
    elif place == 59:
        e9 = token
    elif place == 50:
        e10 = token

    elif place == 61:
        f1 = token
    elif place == 62:
        f2 = token
    elif place == 63:
        f3 = token
    elif place == 64:
        f4 = token
    elif place == 65:
        f5 = token
    elif place == 66:
        f6 = token
    elif place == 67:
        f7 = token
    elif place == 68:
        f8 = token
    elif place == 69:
        f9 = token
    elif place == 60:
        f10 = token

    elif place == 71:
        g1 = token
    elif place == 72:
        g2 = token
    elif place == 73:
        g3 = token
    elif place == 74:
        g4 = token
    elif place == 75:
        g5 = token
    elif place == 76:
        g6 = token
    elif place == 77:
        g7 = token
    elif place == 78:
        g8 = token
    elif place == 79:
        g9 = token
    elif place == 70:
        g10 = token

    elif place == 81:
        h1 = token
    elif place == 82:
        h2 = token
    elif place == 83:
        h3 = token
    elif place == 84:
        h4 = token
    elif place == 85:
        h5 = token
    elif place == 86:
        h6 = token
    elif place == 87:
        h7 = token
    elif place == 88:
        h8 = token
    elif place == 89:
        h9 = token
    elif place == 80:
        h10 = token

    elif place == 91:
        i1 = token
    elif place == 92:
        i2 = token
    elif place == 93:
        i3 = token
    elif place == 94:
        i4 = token
    elif place == 95:
        i5 = token
    elif place == 96:
        i6 = token
    elif place == 97:
        i7 = token
    elif place == 98:
        i8 = token
    elif place == 99:
        i9 = token
    elif place == 90:
        i10 = token

    elif place == 101:
        j1 = token
    elif place == 102:
        j2 = token
    elif place == 103:
        j3 = token
    elif place == 104:
        j4 = token
    elif place == 105:
        j5 = token
    elif place == 106:
        j6 = token
    elif place == 107:
        j7 = token
    elif place == 108:
        j8 = token
    elif place == 109:
        j9 = token
    elif place == 100:
        j10 = token

    else:
        print('Invalid placement')

place_fire()

print_board1()

place_fire()

print_board1()

# Attack
# Ship check
# Record hit or miss

# For player 2
# Attack
# Ship check
# Record hit or miss
