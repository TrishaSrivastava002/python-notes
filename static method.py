class Calculator:

    # A static method is also a method that is bound to the class and not the object of the class.
    #  This method can't access or modify the class state. 
    # It is present in a class because it makes sense for the method to be present in class.
    #  Let's create addNumbers static method
    @staticmethod
    def addNumbers(x, y):
        return x + y

print('Product:', Calculator.addNumbers(15, 110))