import random
from tkinter import *

root = Tk()
root.geometry("300x500")
root.title("Racko")
root.configure(background="blue")

use_new = False
use_discard = False


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

def update_new_card():
    global new_card, use_new
    new_card = draw_new_card()
    new.config(text=new_card)
    use_new = True


def use_discard_card():
    global use_new, use_discard
    if use_new:
        discarded_cards.append(new_card)
        new.config(text="  ")
        discard.config(text=discarded_cards[-1])
        slot1 = 0
        opponents_move(slot1)
        discard.config(text=discarded_cards[-1])
        winner()
        print(opponent_cards)
        use_new = False
    else:
        use_discard = True


def select_card(number):
    global use_discard, use_new
    if use_new:
        card = new_card
        discarded_cards.append(player_cards[number])
        new.config(text="  ")
        use_new = False
    elif use_discard:
        card = discarded_cards[-1]
        discarded_cards.remove(card)
        place_holder = player_cards[number]
        discarded_cards.append(place_holder)
        use_discard = False
    player_cards[number] = card
    # player_update(number)
    slot1 = 0
    opponents_move(slot1)
    discard.config(text=discarded_cards[-1])
    update_all_cards()
    winner()
    print(opponent_cards)

def update_all_cards():
    fift.config(text=player_cards[9])
    ff.config(text=player_cards[8])
    frt.config(text=player_cards[7])
    trf.config(text=player_cards[6])
    trt.config(text=player_cards[5])
    tf.config(text=player_cards[4])
    two.config(text=player_cards[3])
    of.config(text=player_cards[2])
    one.config(text=player_cards[1])
    five.config(text=player_cards[0])



def winner():
    if player_cards == sorted(player_cards):
        you_win()
    elif opponent_cards == sorted(opponent_cards):
        you_lose()


def you_win():
    top = Toplevel()
    top.geometry("+300+300")
    top.title("Winner")
    top.configure(background="blue")
    winner_label = Label(top, text="You Won!", bg="blue", fg="white")
    winner_label.grid(row=0, column=0)
    top.mainloop()


def you_lose():
    top = Toplevel()
    top.geometry("+300+300")
    top.title("Loser")
    top.configure(background="blue")
    winner_label = Label(top, text="You Lost!", bg="blue", fg="white")
    winner_label.grid(row=0, column=0)
    top.mainloop()


def clear_cards():
    global discarded
    player_cards.clear()
    deck.clear()
    opponent_cards.clear()
    deal_cards()
    discarded = " "
    discard.config(text=discarded)


    update_all_cards()

deal_cards()
# print(opponent_cards)


fift = Button(root, text=player_cards[9], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(9))
fift.grid(row=0, column=1, columnspan=2)
fifty_label = Label(root, text="50", bg="blue", fg="white")
fifty_label.grid(row=0, column=0)

ff = Button(root, text=player_cards[8], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(8))
ff.grid(row=1, column=1, columnspan=2)
four_five_label = Label(root, text="45", bg="blue", fg="white")
four_five_label.grid(row=1, column=0)

frt = Button(root, text=player_cards[7], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(7))
frt.grid(row=2, column=1, columnspan=2)
forty_label = Label(root, text="40", bg="blue", fg="white")
forty_label.grid(row=2, column=0)

trf = Button(root, text=player_cards[6], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(6))
trf.grid(row=3, column=1, columnspan=2)
three_five_label = Label(root, text="35", bg="blue", fg="white")
three_five_label.grid(row=3, column=0)

trt = Button(root, text=player_cards[5], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(5))
trt.grid(row=4, column=1, columnspan=2)
thrt_label = Label(root, text="30", bg="blue", fg="white")
thrt_label.grid(row=4, column=0)

tf = Button(root, text=player_cards[4], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(4))
tf.grid(row=5, column=1, columnspan=2)
two_five_label = Label(root, text="25", bg="blue", fg="white")
two_five_label.grid(row=5, column=0)

two = Button(root, text=player_cards[3], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(3))
two.grid(row=6, column=1, columnspan=2)
two_label = Label(root, text="20", bg="blue", fg="white")
two_label.grid(row=6, column=0)

of = Button(root, text=player_cards[2], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(2))
of.grid(row=7, column=1, columnspan=2)
one_five_label = Label(root, text="15", bg="blue", fg="white")
one_five_label.grid(row=7, column=0)

one = Button(root, text=player_cards[1], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(1))
one.grid(row=8, column=1, columnspan=2)
one_label = Label(root, text="10", bg="blue", fg="white")
one_label.grid(row=8, column=0)

five = Button(root, text=player_cards[0], bg="red", fg="white", padx=10, pady=10, command=lambda: select_card(0))
five.grid(row=9, column=1, columnspan=2)
five_label = Label(root, text="5", bg="blue", fg="white")
five_label.grid(row=9, column=0)

discard = Button(root, text=discarded, bg="red", fg="white", padx=10, pady=10, command=use_discard_card)
discard.place(x=150, y=250)
discard_label = Label(root, text="Discard", bg="blue", fg="white")
discard_label.place(x=100, y=250)

new = Button(root, bg="red", text=new_card, fg="white", padx=10, pady=10, command=update_new_card)
new.place(x=150, y=150)
new_label = Label(root, text="Draw", bg="blue", fg="white")
new_label.place(x=100, y=150)

deal = Button(root, text='Deal', bg="green", fg="white", padx=10, pady=10, command=clear_cards)
deal.place(x=150, y=450)


root.mainloop()
