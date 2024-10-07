# Random Password Generator

import random
import string
import playsound

# length = int(input("Enter the desired password length: "))

# chars = string.ascii_letters + string.digits + string.punctuation

# print(chars)

# password = ''.join(random.choice(chars) for i in range(length))

# print(password)


#------------------------------------------------------------------------
# Random Lottery Number Picker

# lottery_numbers = random.sample(range(1, 50), 6)

# print(lottery_numbers)

#-------------------------------------------------------------------------
# Shuffle a deck of cards

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

# deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
deck =[]
for rank in ranks:
    for suit in suits:
        deck.append(f"{rank} of {suit}") # adding to the list 

random.shuffle(deck)

# draw 5 cards
drawn_cards = random.sample(deck, 5)
print("Your hand is: ", drawn_cards)

# Random a song selector

playlist = []
song = random.choice(playlist)
print("Now playing: ", song)
playsound('/path/note.mp3')