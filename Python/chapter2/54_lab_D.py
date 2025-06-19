class Person:
    def __init__(self,name,age):
        """Initialize the person class with common personal details such as name and argument."""
        self.name=name
        self.age=age

    def display_personal_details(self):
        return f"Name : {self.name}, Age :{self.age}"
    
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.employee_id=employee_id
        self.salary=salary
    def display_employee_details(self):
        personal_details=self.display_personal_details()
        return f"{personal_details}, Employee ID : {self.employee_id}, Salary : {self.salary:.2f}"
# Task 3: Define the Derived Class Manager
class Manager(Person):
    def __init__ (self,name,age,department,team_size):
        super().__init__(name,age)
        self.department=department
        self.team_size=team_size
    def display_manager_details(self):
        personal_details=self.display_personal_details()
        return f"{personal_details}, Department: {self.department}, Team Size: {self.team_size}"
#Task 4: Instantiate Objects from the Manager Class
if __name__=="__main__":
    employee=Employee("gagan",21,"E12345",50000)

    manager=Manager("Deep Manager", 25,"Import Export",40)

    print("Employee Details :")
    print(employee.display_employee_details())

    print("\n Manager Details:")
    print(manager.display_manager_details())      