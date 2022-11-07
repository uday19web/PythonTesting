# Classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# Methods, class variables, instance variables, constructor, etc.
# objects for your classes.
'''
self keyword is mandatory for calling variables names into method
instance and class variables have whole different purpose
instance variables attached to the object that creating from the class
constructor name should be __init__
'''
class Calculator:
    num = 100
    # Default constructor
    def __init__(self, a, b):
        # both are instance variable
        # self are nothing but object like we create obj for class
        # obj is called to self
        self.a = a
        self.b = b
        print("I am called automatically when object is created")

    def getdata(self):
        print("I am now executing as a method in class")

    def summation(self):
        return self.a + self.b + Calculator.num # we can call Calculator.num or self.num



obj = Calculator(4, 5) # syntax to create object in python
obj.getdata() # calling the method by bracket at the end
print(obj.num) # call the print
print(obj.summation())

# object with arguments
argu = Calculator(2, 3)
print(argu.summation())