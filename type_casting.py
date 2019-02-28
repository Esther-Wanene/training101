# type casting is changing an integer to be a string
# i.e passing Esther + 354 will give an error because Esther is a string and 345 is an int
# we convert 354 into a string by str() method
marks = 345
marks = str(345)
# will show that marks is of type string
print(type(marks))
details = "Esther" + " " + str(354)
print(details)
# changing some strings to be an integer
marks =int(marks)
# changing integer to boolean
# boolean is mostly used in conditional statements
# as long as a value is not zero it will be true
print(bool(marks))
# zero prints false
print(bool(0))
if True:
    print("executes when true")
else:
    print("executes when false")
