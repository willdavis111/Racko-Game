
from tkinter import *

import player
from player import *
root = Tk()
root.geometry("300x500")
root.title("Racko")
root.configure(background="blue")

use_new = False
use_discard = False


def update_new_card():
    global new_card, use_new
    new_card = player.draw_new_card()
    new.config(text=new_card)
    use_new = True


def use_discard_card():
    global use_new, use_discard
    if use_new:
        discarded_cards.append(new_card)
        new.config(text="  ")
        discard.config(text=discarded_cards[-1])
        slot1 = 0
        player.opponents_move(slot1)
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
    player.opponents_move(slot1)
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
    # discard.config(text=discarded_cards[-1])


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
    player_cards.clear()
    deck.clear()
    opponent_cards.clear()
    player.deal_cards()
    update_all_cards()

player.deal_cards()
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
