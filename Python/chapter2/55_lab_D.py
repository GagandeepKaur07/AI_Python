# Task 1: Define the Base Class Item
class Item:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity
    def display(self):
        print(f"Item : {self.name} , Quantity : {self.quantity}")
# Task 2: Define the Derived Class PerishableItem
class PerishableItem(Item):
    def __init__(self,name,quantity,expiration_date):
        super().__init__(name,quantity)
        self.expiration_date=expiration_date
    def display(self):
        super().display()
        print(f"Expiration Date : {self.expiration_date}")

# Task 3: Define the Derived Class NonPerishableItem
class NonPerishableItem(Item):
    def display(self):
        super().display()
        print("This is non_perishable item.")

# Task 4: Instantiate Objects and Display Item Details
apple=PerishableItem("Apple",10,"2024-10-15")
canned_beans=NonPerishableItem("Canned Beans",20)

print("perishable item Details:")
apple.display()

print("\n Non perishable item Details :")
canned_beans.display()
