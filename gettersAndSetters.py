# Getters and Setters in Python
# are used to access and modify the attributes of a class in a controlled way.
class Employee:
    def __init__(self, firstName, lastName):
        self._firstName = firstName  # Using a single underscore to indicate a protected attribute
        self._lastName = lastName

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        if isinstance(value, str) and value.isalpha():
            self._firstName = value
        else:
            raise ValueError("First name must be a string containing only letters.")

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        if isinstance(value, str) and value.isalpha():
            self._lastName = value
        else:
            raise ValueError("Last name must be a string containing only letters.")

    def getClassVariables(self):
        print(f"The first variable is {self.firstName}, second variable is {self.lastName}.")
    
employeeObject = Employee("Parth", "Joshi")
employeeObject.getClassVariables()
# Example of using getters and setters
employeeObject.firstName = "John"  # Using the setter to change the first name
employeeObject.lastName = "Doe"  # Using the setter to change the last name
employeeObject.getClassVariables()  # Display the updated values
# Attempting to set an invalid value will raise a ValueError
try:
    employeeObject.firstName = "John123"  # This will raise a ValueError
except ValueError as e:
    print(e)
try:
    employeeObject.lastName = "Doe!"  # This will also raise a ValueError
except ValueError as e:
    print(e)
# The use of getters and setters allows for validation and encapsulation of the class attributes.
# This ensures that the attributes are accessed and modified in a controlled manner, maintaining the integrity of the class.
# This is particularly useful in larger applications where you want to enforce certain rules or constraints on the data.
# In this example, the `firstName` and `lastName` attributes are protected (indicated by the single underscore) and can only be accessed through their respective getters and setters.
# This prevents direct access to the attributes and allows for validation when setting new values.
# Using getters and setters is a common practice in object-oriented programming to encapsulate the data and provide controlled access to it.
# This approach helps in maintaining the integrity of the data and allows for future changes without affecting the external interface of the class.
# In summary, getters and setters in Python provide a way to control access to class attributes, allowing for validation and encapsulation.
# This is particularly useful in larger applications where you want to enforce certain rules or constraints on the data.