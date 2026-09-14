# polymorphism
# Polymorphism is a concept in programming that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). 
# In Python, polymorphism can be achieved through method overriding and operator overloading.

# Real-world example: Payment system
class Payment:
    def pay(self, amount):
        raise NotImplementedError('Subclasses must implement this method pay()')
    
# different payment methods
class MPesaPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using MPesa")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in cash")

# same function name but different implementation
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# create different payment methods
mpesa_payment = MPesaPayment()
card_payment = CreditCardPayment()
cash_payment = CashPayment()

# process payments using different methods / polymorphism in action
process_payment(mpesa_payment, 1000) # Output: Paid 1000 using MPesa
process_payment(card_payment, 2000) # Output: Paid 2000 using credit card
process_payment(cash_payment, 500) # Output: Paid 500 in cash