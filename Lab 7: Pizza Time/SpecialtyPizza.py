# SpecialtyPizza

from Pizza import *

class SpecialtyPizza(Pizza):
    
    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        if self.size == "S":
            self.price = 12.00
        elif self.size == "M":
            self.price = 14.00
        elif self.size == "L":
            self.price = 16.00
        

    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n" \
		.format(self.size, self.name, self.price)
    

