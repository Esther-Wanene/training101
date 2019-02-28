# a class is a blueprint/prototypr i.e a collection of related properties and methods
class Student:
    # class variables are variales that are shared across all instances
    reg_number = ""
    grade = ""
    total = 0
    average = 0

    def __init__(self, math, eng, swa, sci, sss):
        self.total= self.total_marks(math, eng, swa, sci, sss)

        self.calculate_avg()

    # a function inside a class is called a method
    # you put parameters after self,


    def total_marks(self, math, eng, swa, sci, sss):
        # to access total variable defined in class use self.total
        total = math + eng + swa + sci + sss

    def calculate_avg(self, tots):
        self.average = tots/5
# variable brian is an object of a class
# an object is an instance of a cless

brian = Student()
