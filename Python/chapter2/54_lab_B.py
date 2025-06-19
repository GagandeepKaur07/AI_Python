# Task 1: Define the Base Class Person
class Person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return f"Hello. I'm {self.name}"
    def greet(self):
        "Return a greeting message with the person's name"
        return f"Hello. I am {self.name}"

# Task 2: Define the Base Class Employee
class Employee:
    def __init__(self,employee_id):
        """Initialize the Employee class with the employee's id."""
        self.employee_id=employee_id
    def get_employee_id(self):
        """Return the employee ID."""
        return self.employee_id
#Task 3: Define the Derived Class Manager Using Multiple Inheritance
class Manager(Person,Employee):
    def __init__ (self,name,employee_id):
        """Initialize the Manager class, which inherits from both person and Emplee"""
        Person.__init__(self,name) 
        Employee.__init__(self,employee_id)
 #Task 4: Instantiate Objects from the Derived Class Manager
if __name__ == "__main__":
    manager= Manager ("Ramar Bose","E12345")
    print(manager.greet())
    print(f"Employee ID : {manager.get_employee_id()}")
    
