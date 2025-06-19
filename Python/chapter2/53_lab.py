# Task 1: Define the Abstract Base Class
#define absttract base class
from abc import ABC, abstractmethod
class BillingRecord(ABC):
    @abstractmethod
    def get_bill(self):
        """ Abstract method to get the billing details.
        Subclasses must implement this method"""
        pass

    @abstractmethod
    def update_bill(self,amount):
        """Abstract method to update the billing amount
        Subclasses must implement this method."""
        pass

# task 2 : Define the Concrete Class
# define concrete classes
class PatientBilling(BillingRecord):
    def __init__(self,patient_id,patient_name,billing_amount=0):
        self.patient_id=patient_id
        self.patient_name=patient_name
        self.billing_amount=billing_amount
    def get_bill(self):
        return{
            'patient ID':self.patient_id,
            'Patient name':self.patient_name,
            'Billing Animal': f"{self.billing_amount:2f}"
        }
    def update_bill(self, amount):
        if amount >0:
            self.billing_amount +=amount
            print(f"Billing amount updated by {amount:.2f}.New amount is {self.billing_amount:.2f}")
        else:
            print("Amount to update must be positive.")
# Task 3: Use the Concrete Class
if __name__ =="__main__":
    patient_bill=PatientBilling(
        patient_id="p001",
        patient_name="Ramar Bose",
        billing_amount=150.00
    )            
    print("Initial Bill Details:")
    print(patient_bill.get_bill())

    patient_bill.update_bill(500.00)
    print("\n Updated bill Details:")
    print(patient_bill.get_bill())
