# import the class from the oops file
from OOPS_In_Python import Calculator

# create the "Inheritance" from parent class "calculator" to child class "ChildImpl"
class ChildImpl(Calculator):
    num2 = 200
    def __init__(self):
        # need create the constructor if it is created in the parent class
        Calculator.__init__(self, 2, 10)

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()

obj = ChildImpl()
print(obj.getcompletedata())

