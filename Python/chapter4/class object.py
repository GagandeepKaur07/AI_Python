class Car:
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def about(self):
        print('Name :', self.Name, 'Amount :', self.Amount)

car1 = Car('Thar', 500000)
car2 = Car('fortuner', 10000000)

car1.Name = 'OD'

car1.about()
car2.about()


    

