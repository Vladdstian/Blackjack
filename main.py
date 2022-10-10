import random
import art

# Blackjack Game

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def create_player(name):
    player = {
        'name': name,
        'cards': [],
        'score': 0
    }
    for _ in range(2):
        card = random.choice(cards)
        player["cards"].append(card)
        player['score'] += card
    return player


def add_card(player):
    new_card = random.choice(cards)
    player['cards'].append(new_card)
    player['score'] += new_card
    print(f"\n{player['name']} drew {new_card} from the deck.")
    print(f"{player['name'].title()} cards: {player['cards']}, current score: {player['score']}")


def blackjack(player_1, player_2):
    if player_1['score'] == player_2['score'] == 21:
        print("BLACKJACK! Draw! What are the chances? ")
        return True
    elif player_1['score'] == 21:
        print(f"BLACKJACK! {player_1['name'].title()} wins!")
        return True
    elif player_2['score'] == 21:
        print(f"BLACKJACK! {player_2['name'].title()} wins!")
        return True
    else:
        return False


def final_cards(player_1, player_2):
    print(f"Your final hand: {player_1['cards']}, final score: {player_1['score']}")
    print(f"Computer's final hand: {player_2['cards']}, final score: {player_2['score']}")


while True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        print(art.logo)
        player = create_player("Player")
        computer = create_player("Computer")
        print(f"Your cards: {player['cards']}, current score: {player['score']}")
        print(f"Computer's first card: {computer['cards'][0]}")
        if not blackjack(player, computer):
            while True:
                choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if choice == 'y':
                    add_card(player)
                    if player['score'] > 21:
                        print(f"\n{player['name']} went over 21! {computer['name']} wins")
                        break
                else:
                    while computer['score'] <= player['score']:
                        add_card(computer)
                    if computer['score'] > 21:
                        print(f"\n{computer['name']} went over 21! {player['name']} wins!")
                    elif player['score'] == computer['score']:
                        print("\nDraw")
                    elif player['score'] > computer['score']:
                        print("\nYou win!")
                    else:
                        print("\nYou loose!")
                    break
        final_cards(player, computer)
        print()
    else:
        print("Goodbye!")
        break
