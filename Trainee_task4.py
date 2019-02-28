#Ask the user for a number. Depending on whether the number is even or odd, print
#out an appropriate message to the user. Hint: how does an even / odd number react
#differently when divided by 2?
#Extras:
#1. If the number is a multiple of 4, print out a different message.#

# the input is always in form of a string and thus has to be converted to int

random_number = int(input("Enter any number to continue: "))

if random_number % 4 == 0:
    print("You entered a multiple of 4.")
elif random_number % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")
