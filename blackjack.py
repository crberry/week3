# Game of Blackjack
# By Chris Berry

# First bits of code are from class

import random

SUITS = "\u2663 \u2665 \u2666 \u2660".split()
FACES = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

deck = []
for suit in SUITS:
  for face in FACES:
    deck.append(face+suit)


# I stole the calculate function from you and modified it.
# Everything else is mine
def calculate_score(cards):
  value = 0
  for card in cards:
    face = card[:-1]
    if face in ['J', 'Q', 'K']:
      points = 10
    elif face == 'A':
      points = 11
    else:
      points = int(face)
    value += points
  for card in cards:  #modified to treat aces appropriately
    face = card[:-1]
    if face=='A' and value>21:
      value = value-10
  return value

# The rest I wrote independently
play="y"
while play=="y":
  random.shuffle(deck)
  player_hand = deck[0:2]
  dealer_hand = deck[2:4]
  print("Your hand is",player_hand,"\n")
  print("Dealer is showing",deck[3:4],"\n")
  cardnum = 4
  Xstr = input("Would you like another card (y/n)? ")
  while Xstr == "y":
    player_hand=player_hand+deck[cardnum:cardnum+1]
    print(player_hand,"\n")
    cardnum = cardnum + 1
    Xstr = input("Would you like another card (y/n)? ")
  print("\n Your hand is",player_hand,"\n")
  player_score = calculate_score(player_hand)
  print("Your total points are",player_score,"\n")
  if player_score>21:
    print("You Busted!")
  elif player_score==21:
    print("You Won!")
  else:
    print("Now it's the dealer's turn \n")
    print("The dealer's hand is",dealer_hand,"\n")
    dealer_score = calculate_score(dealer_hand)
    while dealer_score < 17:
      dealer_hand = dealer_hand+deck[cardnum:cardnum+1]
      print(dealer_hand,"\n")
      cardnum=cardnum+1
      dealer_score = calculate_score(dealer_hand)
    print("The dealer's score is",dealer_score,"\n")
    if dealer_score==player_score:
      print("Tie goes to the dealer. You lose.") # Vegas rules
    elif dealer_score < player_score:
      print("You win")
    elif dealer_score>21:
      print("Dealer busts. You win!")
    else:
      print("You lose")
  play = input("\n Would you to play again (y/n)? ")



