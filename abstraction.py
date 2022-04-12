

from abc import ABC, abstractmethod
class car(ABC): # parent class
    def paySlip(self,amount):
        print('Your purchase amount:',amount)
    @abstractmethod
    def payment(self,amount):
        pass

class CreditCardPayment(car): #child class
    def payment(self,amount):
        print('Your purchase amount of {} exceeded your $100 limit.'.format(amount))

obj = CreditCardPayment()
obj.paySlip('$400')
obj.payment('$400')

            
