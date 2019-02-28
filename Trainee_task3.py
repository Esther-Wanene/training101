#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
#makes a new list of only the first and last elements of the given list. For practice,
#write this code inside a function

# define the list you want to use as input
a = [7,5, 10, 15, 20, 25]

# function to slice the list with parameter x


def slice_list(x):
    # assign a new variable to represent the new list
    # x[0] reps first element of the list and x[-1] reps the last element of the list
    #
    new_list = [x[0], x[-1]]
    return new_list


print(slice_list(a))


