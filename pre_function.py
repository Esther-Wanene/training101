student1 = [85, 82, 78, 65, 66]
student2 = [73, 42, 84, 52, 55]
student3= [55, 74, 92, 86, 100]
student4 = [20, 21, 75, 58, 87]
student5 = [79, 80, 90, 76, 85]
# a function is a block of code that is used to print a related function

#this function goes through the marks of each student stored in list


def total(z):
    b = sum(z)
    return b


def avg(y):
    a = total(y)/5
    return a


def calculate_grade(x):
    avg1 = avg(x)
    if avg1 >= 90 and avg1 < 101:
        return "A"
    elif avg1 >= 80:
        return "B"
    elif avg1 >= 70:
        return "C"
    elif avg1 >= 60:
        return "D"
    else:
        return "E"


# print("Student1: ", calculate_grade(student1))
# print("Student2: ", calculate_grade(student2))
# print("Student3: ", calculate_grade(student3))
# print("Student4: ", calculate_grade(student4))
# print("Student5: ", calculate_grade(student5))

# total1 = sum(student1)
# avg1 = total1 / 5
# if avg1 >= 90 and avg1 < 101:
#     print("Student1: A")
# elif avg1 >= 80:
#     print("Student1: B")
# elif avg1 >= 70:
#     print("Student1: C")
# elif avg1 >= 60:
#     print("Student1: D")
# else:
#     print("Student1: E")
#
# total2 = sum(student2)
# avg2 = total2 / 5
# if avg2 >= 90 and avg2 < 101:
#     print("Student2: A")
# elif avg2 >= 80:
#     print("Student2: B")
# elif avg2 >= 70:
#     print("Student2: C")
# elif avg2 >= 60:
#     print("Student2: D")
# else:
#     print("Student2: E")
#
# total3 = sum(student3)
# avg3 = total3 / 5
# if avg3 >= 90 and avg3 < 101:
#     print("Student3: A")
# elif avg3 >= 80:
#     print("Student3: B")
# elif avg3 >= 70:
#     print("Student3: C")
# elif avg3 >= 60:
#     print("Student3: D")
# else:
#     print("Student3: E")
#
# total4 = sum(student4)
# avg4 = total4 / 5
# if avg4 >= 90 and avg4 < 101:
#     print("Student4: A")
# elif avg4 >= 80:
#     print("Student4: B")
# elif avg4 >= 70:
#     print("Student4: C")
# elif avg4 >= 60:
#     print("Student4: D")
# else:
#     print("Student4: E")
#
# total5 = sum(student5)
# avg5 = total5 / 5
# if avg5 >= 90 and avg5 < 101:
#     print("Student5: A")
# elif avg5 >= 80:
#     print("Student5: B")
# elif avg5 >= 70:
#     print("Student5: C")
# elif avg5 >= 60:
#     print("Student5: D")
# else:
#     print("Student5: E")
#
#
#
#
#
# # for marks in student2:
# #     total2 = sum(student2)
# #     return total2
# #
# # for num in student3:
# #     total3 = sum(student3)
# #     return total3
# #
# # for score in student4:
# #     total4 = sum(student4)
# #     return total4
# #
# # for trial in student5:
# #     total5 = sum(student5)
# #     return total5


