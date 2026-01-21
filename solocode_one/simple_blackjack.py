from random import choices, shuffle


def draw_card(hand, deck):
    hand.append(deck.pop())


def calculate_score(hand: list[str]):
    score = 0
    for card in hand:
        if card.isdigit():  # one of the number ranks
            score += int(card)
        elif card in ["J", "Q", "K"]:  # face cards
            score += 10
        else:  # defer ace scoring to the end
            continue

    if "A" in hand:  # score aces
        if score <= 10:
            score += 11
        else:
            score += 1

    return score


def display_hand(hand):
    hand_score = calculate_score(hand)
    print(f"{hand} ~> {hand_score}")


def main():
    deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    dealer_hand = []
    player_hand = []

    # Shuffle and deal
    shuffle(deck)

    # The player gets two cards at the start, dealer draws one after
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)
    draw_card(dealer_hand, deck)

    while True:
        # show the hands
        print("Player hand: ")
        display_hand(player_hand)
        print("Dealer hand: ")
        display_hand(dealer_hand)

        if calculate_score(player_hand) >= 21:
            break

        action = input("Would you like to (h)it or (s)tay? ").lower()
        if action == "h":
            draw_card(player_hand, deck)
        elif action == "s":
            print("The dealer will now draw.")
            break
        else:
            print("Invalid action.")

    if calculate_score(player_hand) > 21:
        print("Player busts!")
        return

    while calculate_score(dealer_hand) <= 17:
        draw_card(dealer_hand, deck)
        print("Dealer hand: ")
        display_hand(dealer_hand)

    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    if dealer_score > 21:
        print("Dealer busts!")
        print("Player wins!")
    elif dealer_score == 21:
        print("Dealer wins!")
    elif player_score == 21:
        print("Player wins!")
    elif calculate_score(dealer_hand) >= calculate_score(player_hand):
        print("Dealer wins!")
    else:
        print("Player wins!")


if __name__ == "__main__":
    main()
