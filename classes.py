
class Vehicle:        # parent class
    make = 'Toyota'
    model = 'Camry'
    year = 2014
    VIN = 93819321

class Sales(Vehicle):   # child class no.1
    price = '$12,699'
    salesperson = 'John Jackson'

class Detailing(Vehicle):  # child class no.2
    Inside_Detailed = True
    Outside_Detailed = True
    Detailing_Company = 'Swiffy Detailing'
