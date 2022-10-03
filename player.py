import random
global new_card, discarded_cards, discarded, opponent_cards
deck = []
discarded_cards = []
player_cards = []
opponent_cards = []
slot = -1
new_card = " "
discarded = " "


def make_deck():
    global deck
    deck = []
    for n in range(1, 61):
        deck.append(n)


def deal_cards():
    global deck, player_cards, opponent_cards
    make_deck()
    for pc in range(1, 11):
        player_cards.append(random.choice(deck))
        deck.remove(player_cards[-1])
    for pc in range(1, 11):
        opponent_cards.append(random.choice(deck))
        deck.remove(opponent_cards[-1])
    opponent_cards.insert(0, 0)
    opponent_cards.append(61)


def draw_new_card():
    global new_card
    new_card = random.choice(deck)
    deck.remove(new_card)
    return new_card


def use_card(slot, card_choice, disc):
    holder = opponent_cards[slot]
    opponent_cards[slot] = card_choice
    discarded_cards.append(holder)
    if disc == 1:
        discarded_cards.remove(card_choice)


def use_card_opponent(slot2, card_choice):
    holder = opponent_cards[slot2]
    opponent_cards[slot2] = card_choice
    discarded_cards.append(holder)
    # print(slot2)
    # print(discarded_cards)


def opponents_move(slot1):
    order_eval(slot1, discarded_cards[-1])
    if card_used:
        discarded_cards.remove(discarded_cards[-2])
        # print(discarded_cards)
    else:
        order_eval(slot1, draw_new_card())


def order_eval(slot, card_choice):
    global card_used
    card_used = True
    for x in opponent_cards:
        slot += 1
        if (slot * 6) >= card_choice > float((slot-1) * 6):
            if (slot * 6) >= opponent_cards[slot] > float((slot - 1) * 6):
                if card_choice > opponent_cards[slot] and opponent_cards[slot + 1] != 61:
                    use_card_opponent(slot + 1, card_choice)
                elif card_choice < opponent_cards[slot] and opponent_cards[slot-1] != 0:
                    use_card_opponent(slot - 1, card_choice)
                else:
                    card_used = False
            else:
                use_card_opponent(slot, card_choice)





