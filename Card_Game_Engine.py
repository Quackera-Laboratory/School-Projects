import random

#Game specific tweaks
joker_card = False

cards_per_player = 5
#End of specfic teaks
    
suits = ["♥", "♠", "♦", "♣"]

ranks = [
    "Ace", "2", "3", "4", "5", "6", "7",
    "8", "9", "10", "Jack", "Queen", "King"
]

cards = []

# Each individual card is formed by a combined two-element list. For Translating I want to turnt his into a class instead.

for card_value in ranks:
    for suit in suits:
        cards.append([card_value, suit])

# creates the deck by going through each value of each suit and rank indivually. 13 * 4 (=52) cards and not a direct 52 cards, and jokers can be appended if enabled.

if joker_card:
    cards.append(["Joker", "★"])
    cards.append(["Joker", "★"])

random.shuffle(cards)

#randomizes cards AFTER any engine changes for a given title.

print(cards)
print("Total cards:", len(cards))

gamemode = int(input("How many human players? "))

players = []

#interpreted list that will likely be a pita for C# that contains player names. ex 0, Blaze | 1, Player2 | 2, Player3 | 3, CPU, but then with +1 to make the list 1, Blaze | 2, Player2 | 3, Player3 | 4, CPU

for player_number in range(gamemode):
    name = input(f"Who is Player {player_number + 1}?\n")
    players.append(name)
    print("players")

desired_players = int(input("How many total players are desired?"))
while len(players) < desired_players:
    players.append("CPU")

hands_per_player = 1

player_piles = [
    [[] for _ in range(hands_per_player)]
    for _ in range(len(players))
]

# nested list containing lists of piles, which themselves contain cards e inner comprehension creates the requested number of empty piles. The outer comprehension repeats that process for every player

def deal_cards(cards, player_piles, cards_per_player):
    for card_number in range(cards_per_player):
        for player_number in range(len(player_piles)):
            player_piles[player_number][0].append(cards.pop())
            #deals cards to all players

def player_deal(cards, player_piles, player_number):
    player_piles[player_number][pile_number].append(cards.pop())
    #adds a single card to the players hand

deal_cards(cards, player_piles, cards_per_player)

print(player_piles[0])
