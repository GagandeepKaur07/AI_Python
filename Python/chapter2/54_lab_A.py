class Employee:
    def __init__(self,name,employee_id,salary):
        """Initilize the Employee class with common detail such as name, ID, and salary."""
        self.name=name
        self.employee_id=employee_id
        self.salary=salary
    def display_details(self):
        """Display the employee's details."""
        return f"Employee Name: {self.name}\n Employee ID: {self.employee_id}\n Salary : {self.salary:.2f}"
# Task 2: Define the Derived Class Manager
class Manager(Employee):
    def __init__(self,name,employee_id,salary,team_size):
        """Initialize the Manager class, Which inherits from Employee and adds the team size attibute."""
        super().__init__(name,employee_id,salary)
        self.team_size=team_size
    def display_details(self):
        """Display the manager's details, including team size"""
        employee_details=super().display_details()
        return f"{employee_details}\n Team size : {self.team_size}"
# Task 3: Instantiate Objects from Base and Derived Classes

if __name__ =="__main__":
    employee=Employee("Employee","E001",5000)

    manager= Manager("Manager","M456",80000,10)
    
    print("Employee Details:")
    print(employee.display_details())

    print("\n Manager Details:")
    print(manager.display_details())