import random

#Game specific tweaks
joker_card = False

cards_per_player = 2
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

gamemode = int(input("How many human players? "))

players = []

player_hands = [[], [], []]


for player_number in range(gamemode):
    name = input(f"Who is Player {player_number + 1}?\n")
    players.append(name)
    print("players")

desired_players = int(input("How many total players are desired?"))
while len(players) < desired_players:
    players.append("CPU")

player_states = ["playing" for _ in range(len(players))]



player_hands = [[] for _ in range(desired_players)]
print(players)

def initial_deal(cards, player_hands, cards_per_player):
    for card_number in range(cards_per_player):
        for player_number in range(len(player_hands)):
            player_hands[player_number].append(cards.pop())

def deal_cards(cards, player_hands, cards_per_player):
    for card_number in range(1):
        for player_number in range(len(player_hands)):
            player_hands[player_number].append(cards.pop())
            #deals one card to all players

def player_deal(cards, player_hands, player_number):
    player_hands[player_number].append(cards.pop())
    #adds a single card to the players hand

#Keep this outside the player-turn loop but inside a larger turn-loop.
initial_deal(cards, player_hands, cards_per_player)

#Start the turn logic to go through all players, and storing their answers as unique values.
BlackJack_game_logic = True
while BlackJack_game_logic == True:
    for player_number in range(len(players)):
        
        while player_states[player_number] == "playing":
        
            print(players[player_number], "hand:", player_hands[player_number])
            print("hit, double down, stand/stay, or split?\n")
        
            current_action = input(players[player_number] )
        
            if current_action.lower() == "hit" or current_action == "1":
                player_deal(cards, player_hands, player_number)
            elif current_action.lower() == "double" or current_action == "2":
                player_deal(cards, player_hands, player_number)
                player_states[player_number] = "standing"
            elif current_action.lower() == "stand" or current_action.lower() == "stay" or current_action == "3":
                player_states[player_number] = "standing"
                print(players[player_number], player_hands[player_number])
                
            elif current_action.lower() == "split" or current_action == "4":
                print("splitting is not currently functional.")
                player_deal(cards, player_hands, player_number)*2
        
        #I now need some form of check to for "split" elswise I .pop all cards
            
        #I need to eventually figure out a repeating deck that is random but can only pull from the removed. list. may require an additional append to a new list


        #start of next turn deal_cards(cards, player_hands, cards_per_player)
