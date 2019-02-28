# a string is an array of characters.
# used to pass information within a python program
my_first_string= "hello world"
# capitalize the first letter of the string. The capitalize will print Hello world
print(my_first_string.capitalize())
# upper makes every letter of the string capital
print(my_first_string.upper())
# make every letter lowercase
print(my_first_string.lower())
# this line of code returns the number of letter o's in the string. define o as 'o'
print(my_first_string.count('o'))
# will print the length of the string
print(len(my_first_string))
# define two variables in a single statement
first_name, second_name = "Esther", "Wanene"
# the following code is how you join two strings together
"""the " " with a space between the two variables creates a space between 
the two joined variables(concatenating two strings)"""
full_name = first_name + " " + second_name
print(full_name)
# get the first letter of the string full name
first_letter = full_name[0]
# get the last letter
last_letter = full_name[-1]
# get the last letter
last_letter = [len(full_name)-1]
print(first_letter)
# The islower() methods returns “True” if all characters in the string are lowercase, Otherwise, It returns “False”.
print(first_letter.islower())
