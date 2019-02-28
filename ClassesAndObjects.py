# class Card(object):
#     balance = 0
#
#     def __init__(self, bal):
#         self.balance = bal
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return self.print_receipt(self.balance, amount)
#
#         else:
#             return "Insufficient balance"
#
#     def print_receipt(self, balance, withdraw):
#         return """AMOUNT :....{}
# BALANCE: ....{}""".format(balance, withdraw)


class Library(object):
    genre = []
    books = 0
    members = []

    def __init__(self, gen, bks, mems):
        self.genre = gen
        self.books = bks
        self.members = mems
    def lend(self):
        self.books -= 1