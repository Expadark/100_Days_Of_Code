logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(card_list):
    card_list.append(random.choice(cards))
def show_scores():
    print(f"Your Cards are {player_cards} , total score : {player_score}")
    print(f"Dealer shows {dealer_cards[0]}")
def go_again():
    da = input("Do you want another card? Type 'y' or 'n' ")
    if da == "y":
        deal_card(player_cards)
    elif da == "n":
        draw_again = False

play_again = True

while play_again:
    print(logo)
    player_cards = []
    dealer_cards = []
    draw_again = True
    game_over = False

    deal_card(player_cards)
    deal_card(player_cards)
    deal_card(dealer_cards)
    deal_card(dealer_cards)

    while draw_again:
        player_score = 0
        dealer_score = 0
        for card in dealer_cards:
            dealer_score += card
        for card in player_cards:
            player_score += card

        if player_score > 21:
            if 11 in player_cards:
                player_score -= 10
                if player_score > 21:
                    show_scores()
                    print("You busted, Game Over")
                    draw_again = False
                    game_over = True
                else:
                    show_scores()
                    da = input("Do you want another card? Type 'y' or 'n' ")
                    if da == "y":
                        deal_card(player_cards)
                    elif da == "n":
                        draw_again = False
            else:
                show_scores()
                print(f"Dealer shows {dealer_cards}")
                print("You busted, Game Over")
                draw_again = False
                game_over = True
        elif player_score == 21 and not dealer_score == 21:
            show_scores()
            print("21, you win")
            draw_again = False
            game_over = True
        elif dealer_score == 21:
            draw_again = False
            show_scores()
            print("Dealer at 21, you lose")
            game_over = True
        else:
            show_scores()
            da = input("Do you want another card? Type 'y' or 'n' ")
            if da == "y":
                deal_card(player_cards)
            elif da == "n":
                draw_again = False

    if not game_over:
        print(f"Dealer shows {dealer_cards} for {dealer_score}")
        while dealer_score < 16:
            dealer_score = 0
            deal_card(dealer_cards)
            for card in dealer_cards:
                dealer_score += card
            print(f"Dealer shows {dealer_cards} for {dealer_score}")
        if dealer_score > player_score:
            print(f"Dealer wins with {dealer_score}")
        elif dealer_score < player_score:
            print(f"Player wins with {player_score}")
        elif dealer_score == player_score:
            print("Draw")

    pg = input("Do you want to play again? 'y' or 'n'")
    if pg == "y":
        os.system('cls')
    else:
        play_again = False