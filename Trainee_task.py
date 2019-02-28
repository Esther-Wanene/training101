###Write a program which accepts a string as input to print "Yes" if the string is "yes",
#"YES" or "Yes", otherwise print "No".
#Hint: Use input () to get the persons input

open = input("Would you please open the door for me: ")

if open == 'YES' or open == 'yes' or open == 'Yes':
    print("Yes")
else:
    print("No")

