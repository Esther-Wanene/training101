#With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first
#half values in one line and the last half values in one line.

a = (0,1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14)
# range does not include the last number thus will print from index 0 to four
# y = a[:5]
# # will return from index 5 to the end
# z = a[6:]
# print(y)
# print(z)
# #b =(len(a)/2)
y = a[: int(len(a)/2)]
#
print(y)

z = a[int(len(a)/2):]
print(z)
