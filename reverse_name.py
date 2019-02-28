# write a code that takes in your name and reverses it
# get name from user
name = input("Please enter your name: ")


def reverse_my_name(my_name):
    reverse_name = my_name[::-1]
    return reverse_name
# pass argument name to be reversed


print(reverse_my_name(name))




