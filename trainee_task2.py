#TASK 2:
#Implement a function that takes as input three variables, and returns the largest of
#the three. Do this without using the Python max () function!
#The goal of this exercise is to think about some internals that Python normally takes
#care of for us.


#create three variables
a= input("Enter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

# a function that will find the largest between two variables and if some numbers are equal returns one of them


def max_of_two(x, y):
    if x > y:
        return x
    elif x == y:
        return y
    else:
        return y


def max_of_three(x, y, z):
    if x == z or y == z:
        return z
    else:
        return max_of_two(x, max_of_two(y, z))


print("The largest number is", max_of_three(a, b, c))

