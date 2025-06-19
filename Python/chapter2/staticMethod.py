# Task 1: Define the Shopping Cart Class and add items
class ShoppingCart:
    tax_rate=0.08
    def __init__(self):
        self.items=[]
    def add_item(self,name,price):
        self.items.append({'name' : name, 'price ': price})
# Task 2: Calculate Total Price Including Tax
    def calculate_total(self):
        total=sum(item['price '] for item in self.items)
        total_with_tax = total+(total*self.tax_rate)
        return total_with_tax
# The final amount after the discount is applied is returned.
    def apply_discount(self,discount_percentage):
        total = self.calculate_total()
        discount = total*(discount_percentage/100)
        return total - discount
#Task 4: Format Price for Display and Calculate Tax Independently
    
    @staticmethod
    
    def format_price(amount):
        return f"${amount:.2f}"
    
    @staticmethod
    
    def calculate_tax(amount):
        return amount*ShoppingCart.tax_rate

cart=ShoppingCart()
cart.add_item("laptop",50000)
cart.add_item("Headphones",1500)
cart.add_item("Mouse",450)

total_price = cart.calculate_total()
print(f"Total price (include tax) : {ShoppingCart.format_price(total_price)}")

# Apply a discount
discounted_price= cart.apply_discount(10)
print(f"Price after discount : {ShoppingCart.format_price(discounted_price)}")

# Calculated tax on a specific amount
tax_on_laptop=ShoppingCart.calculate_tax(1000)
print(f"Tax on laptop : {ShoppingCart.format_price(tax_on_laptop)}")
