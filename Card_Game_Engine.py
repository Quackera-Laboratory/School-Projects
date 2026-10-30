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

for card_value in ranks:
    for suit in suits:
        cards.append([card_value, suit])

if joker_card:
    cards.append(["Joker", "★"])
    cards.append(["Joker", "★"])

random.shuffle(cards)

print(cards)
print("Total cards:", len(cards))

gamemode = int(input("How many human players? "))

players = []

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

def deal_cards(cards, player_piles, cards_per_player):
    for card_number in range(cards_per_player):
        for player_number in range(len(player_piles)):
            player_piles[player_number][0].append(cards.pop())

def player_deal(cards, player_piles, player_number):
    player_piles[player_number][pile_number].append(cards.pop())
    #adds a single card to the players hand

deal_cards(cards, player_piles, cards_per_player)

print(player_piles[0])
