# from ClassesAndObjects import Card
#
#
# card1 = Card(1000)
#
# my_card = Card(102)
#
# print(my_card.balance)
#
# print(card1.withdraw(100))
# print(card1.balance)

# you parse a method .method(args)
# variable .var no brackets

from ClassesAndObjects import Library

tech_camp_lib = Library(gen=["Sci-fi", "comedy"], bks=1000, mems=["Diana", "Mary"])
print(tech_camp_lib.members)

print(tech_camp_lib.genre)
# runs method lend meaning one book will bro
tech_camp_lib.lend()
print(tech_camp_lib.books)