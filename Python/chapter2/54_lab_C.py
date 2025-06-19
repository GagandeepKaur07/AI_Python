# Task 4: Instantiate Objects from the Derived Class Manager.
class Person:
    def __init__(self,name,age):
        "Initialize the person class with common personal details such as name and age."
        self.name=name
        self.age=age
    def display_personal_details(self):
        "display the person's name and age."
        return f"Name : {self.name} , Age:{self.age}"

# Task 2: Define the Derived Class Employee
class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        """initialization the emloyee class, which inherits from person adds employee details."""
        super(). __init__(name,age)
        self.employee_id=employee_id
        self.salary=salary

    def display_employee_details(self):
        """display employee specific details such as employee ID and salary."""
        personal_details=self.display_personal_details()
        return f"{personal_details}, Employee ID : {self.employee_id}, Salary: {self.salary:.2f}"
    
#Task 3: Define the Further Derived Class Manager
class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department,team_size):
        """Initialize the Manager class, which inherits from Employee and adds manager-specific details."""
        super().__init__(name,age,employee_id, salary)
        self.department=department
        self.team_size=team_size
    def display_manager_details(self):
        "Display manager specifia details along with inherited personal and employee details."
        employee_details=self.display_employee_details()
        return f"{employee_details},Department:{self.department},team size: {self.team_size}"

# Task 4: Instantiate Objects from the Manager Class
if __name__ == "__main__":
    Manager=Manager("Ramar Bose",45,"M12345",95000,"Sales",10)
    print("Manager Details:")
    print(Manager.display_manager_details())