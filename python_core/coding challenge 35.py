from abc import ABC , abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self):
        pass

class CreditCardPayment(PaymentMethod):
    
    def processPayment(self):

        print("Processing payment using Credit Card.")
        

class PayPalPayment(PaymentMethod):
    
    def processPayment(self):

        print("Processing payment using Paypal.")

def process_transaction(payment: PaymentMethod):
    payment.processPayment()

credit = CreditCardPayment()
paypal = PayPalPayment()

process_transaction(credit)
process_transaction(paypal)




