alpha = ["z","y", "x",['duck','says','quack']] #[list[nested list]]
print(alpha[3][2])
alpha[3].pop(2) # alpa[3] sets the grid point to my nested list
print(alpha)
alpha[2] = 1
print(alpha)



for loop in range(4):
    alpha.pop()
    print(alpha)
print(alpha)




dinner = ['Mario', 'Loves', ]

print(dinner)

for letter in "spaghetti":
    dinner.append(letter)
    print(dinner)

print("\n\n", dinner)