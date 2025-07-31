# Below is the example of a basic class and object in Python.
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# A class is defined using the `class` keyword followed by the class name and a colon.
# The class name should follow the CamelCase convention.
# An object is an instance of a class. It is created by calling the class as if it were a function.

class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def getClassVariables(self):
        print(f"The first variable is {self.firstName}, second variable is {self.lastName}.")
    
employeeObject = Employee("Parth", "Joshi")
employeeObject.getClassVariables()


# To inherit any parent class into the child class, we can use the following syntax:
class Employee:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def getClassVariables(self):
        print(f"The first variable is {self.firstName}, second variable is {self.lastName}.")

class Manager(Employee):
    def __init__(self, firstName, lastName, department):
        super().__init__(firstName, lastName)  # Call the parent class constructor
        self.department = department
    
    def getClassVariables(self):
        super().getClassVariables()  # Call the parent class method
        print(f"The department is {self.department}.")