# print("Nairobi")
# # python only accepts indentation only if there is a full colon in the previous line
# print("Mombasa")
# in the below definition equality acts as a boolean and the resolve is false
# this will run the else statement
equality = "Mombasa" == "Nairobi"
# the resolve is true because the length of mombasa and nairobi is 7 characters and thus true
# this will run the if statement
equality = len("Mombasa") == len("Nairobi")
print(equality)
if equality:
    print("Nairobi and Mombasa are the same")
else:
    print("Nairobi is not equal to Mombasa")