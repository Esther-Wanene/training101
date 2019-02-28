# executes a block of statements until a condition is false


# num = []
# for x in range(10):
#     num.append(x)
#     print (num)
#
# i = 0
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.pop()
# # executes until 6 > 6 which is false, since 6 = 6
# while len(numbers)>0:
#     print(numbers)
#     # removes the last number of the list
#     numbers.pop()
#     # increment i by one
# create a system that has a stored password 1234, allows the user to try inputting the password three times.
# if the user fails in all three attempts it prints out pin blocked
# when the user enters the correct password it prints correct pin entered
password_saved = "1234"
tries = 1
max_tries = 3
password = input("Enter your password ")
while password != "1234" and tries < 3:
    max_tries -= 1
    if max_tries < 2 and :
        print("please enter correct password {} trial left".format(max_tries))
    else:
password = input("please enter correct password {} trials left".format(max_tries))
tries += 1

if tries >= 3:
    print("Pin Blocked, we shall hold your card until further notice")
else:
    print("Hurray correct password entered")
