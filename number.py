import random
playing = True
number = str (random.randint(10,20))

print("I will generate a number from 0 to 9, and u have to guess the number one digit at a time")
print("The game ends when u get 1 hero")
while playing:
    guess = input("Give me your best guess. \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break

    else:
        print("Your guess isnt quite right, try again. \n")