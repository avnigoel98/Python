import random



# # coin toss game
# choices = ["Heads", "Tails"]

# player = input("Heads or Tails: ")


# computer  = random.choice(choices)

# print("Player:" , player)
# print("Computer: ", computer)

# if player.upper() == computer.upper():
#     print("You guessed it correct")
# else:
#     print("Sorry, you guessed wrong")

# random integer - randInt
# number = random.randint(1, 6)
# print(number)
# player = int(input("Guess the numebr: "))



# if(player == number):
#     print("Correct")
# else:
#     print("Not Correct")

# rolling a dice


# Odd or Even Game
number = random.randint(10, 100)
print("Computer (number): ", number)
player = input("Odd or even: ")



if number % 2 == 0 and player == "even":
    print("Correct, Even")
elif  number % 2 != 0 and player == "odd":
    print("Correct, Odd")
else:
    print(f"Wrong, the number was {number}")



# / - divison
# % - remainder after division