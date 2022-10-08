import random
import art

# Blackjack Game

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def player_start():
    player = {
        "cards": [],
        "score": 0
    }
    for _ in range(2):
        card = random.choice(cards)
        player["cards"].append(card)
        player["score"] += card
    return player


def add_new_card(player):
    card = random.choice(cards)
    player["cards"].append(card)
    player["score"] += card


def check_score(player):
    if player['score'] > 21:
        print("Bust!")
        return True
    elif player['score'] == 21:
        print("Blackjack!")
        return True
    else:
        return False


def check_winner(p1, p2):
    if p2['score'] < p1['score'] <= 21:
        print(f"Player wins!")
    else:
        print(f"Computer wins!")


# Game start
game_is_on = True
while game_is_on:
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n")
    if game_start == 'y':
        # Game Start
        print(art.logo)
        player = player_start()
        computer = player_start()
        player['score'] = 21
        # TODO - check for score/ Blackjack
        print(f"Your cards: {player['cards']}, current score: {player['score']}")
        print(f"Computer's first card: {computer['cards'][0]}")
        if check_score(player) or check_score(computer):
            print()
            continue
        else:
            # Player draws more cards
            choice = 'y'
            while choice == 'y':
                choice = input("Type 'y' to get another card, type 'n' to pass: ")
                if choice == 'y':
                    add_new_card(player)
                    print(f"Your cards: {player['cards']}, current score: {player['score']}")
                    check
                else:
                    while computer['score'] <= player['score'] and computer['score'] <= 21:
                        add_new_card(computer)
                    print(f"computer final cards: {computer['cards']}, current score: {computer['score']}")
                    check_winner(player, computer)
    else:
        break
