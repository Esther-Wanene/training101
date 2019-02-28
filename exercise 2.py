task_list = [23, "jane", ["Lesson 23", 560, {"currency": "KES"}], 987, (76, "John")]
# 1: Determine the variable type of task_list using an inbuilt function
print(type(task_list))
# 2. Print KES
# get inside index two of task list which is a list thus [2]
# KES is inside the second element of the second list which is a dictionary thus[2]
# thus to access KES we have to use key "currency"
print(task_list[2][2]["currency"])
# 3. Print 560
print(task_list[2][1])
# 4. Use a function to determine the length of the list
length_of_list = len(task_list)
print(length_of_list)
# 5. Change 987 to 789 using an inbuilt function
# 987 is index 3 assign it to a variable c
# convert c to a string
# # reverse c using ::-1 and type cast to convert it back to an int
c = str(task_list[3])
print(int(c[::-1]))

# 6. Change name John to Jane
# name = (str(task_list[4][1]))
# task_list[4][1] = "Jane"
# print(task_list)
# cannot be done because it is a tuple




