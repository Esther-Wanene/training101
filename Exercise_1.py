sentence = "The dog finished the pie"

# write a python program to answer the questions below

# 1. How many words are in the string?(homework)
words = sentence.split()
print("The number of words in the string is", len(words))
# # 2. What is the length of string sentence?
print("The length of the sentence is", len(sentence))
#
# # 3. How many times does the word dog appear
print("The word dog appears", sentence.count('dog'), "time")
#
# # 4. Output the string sentence in reverse order
print(sentence[::-1])
# # 5. Write a new string similar to sentence except that all letters are capital letters
print(sentence.upper())