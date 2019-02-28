empty_string = ""
my_first_number = 0
empty_list = []
noise_makers= ["Brian", "Mike", 9, True]
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_the_week)
number_of_days_in_a_week = len(days_of_the_week)
print(number_of_days_in_a_week)
# list indexing to retrieve the 3rd element: n-1
print(days_of_the_week[2])
# list to retrieve monday to wednesday
print(days_of_the_week[0:3])
# list to retrieve from thursday to sunday
print(days_of_the_week[3:])

details=["Esther", 23, "testingwdg21@outlook.com", "Dublin"]
# to retrieve age
age = details[1]
# to retrieve location
location = details[3]
# output the list in reverse
print(details[::-1])
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print 8 and 9
sub_num = numbers[-3:-1]
print(sub_num)
# append is used to add a value to a list
days_of_the_week.append("val")
print(days_of_the_week)
# you can append a list to another list
# days_of_the_week.append(numbers)
# # the appended list becomes an element
# print(days_of_the_week[-1])
days_of_the_week.extend(numbers)
print("extend", days_of_the_week)

list1= [0, 1]
list2 = [2, 3]
list1.append(list2)
list3 = list1+list2
print(list3)

