# input function is used to get data from the user
# any input you get from the user is in the form of a string and thus you have to convert it to int
marks = int(input("Enter your marks "))
# if else statement
# if marks >= 350:
#     print("Congratulations you have qualified")
# else:
#     print("Sorry you have failed")

# GRADING SYSTEM
average = marks/5
if average >= 80 and average < 101:
    print("A")
elif average >= 70 and average < 80:
    print("B")
elif average >= 60 and average < 70:
    print("C")
elif average >= 50 and average < 60:
    print("D")
elif average < 50 and average >= 1:
    print("E")
elif average > 101:
    print("ISSA LIE")
    exit()
else:
    print("Please enter a valid number")
