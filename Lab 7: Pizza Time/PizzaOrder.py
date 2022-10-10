# PizzaOrder

from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *

class PizzaOrder():

    def __init__(self, time):
        self.time = time
        self.pizzalist = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzalist.append(pizza)
        

    def getOrderDescription(self):
        result = ''
        count = 0.0
        result = result + "******\nOrder Time: {}\n".format(self.time)
        for i in self.pizzalist:
            result += i.getPizzaDetails() + "\n" + "----\n"
            count = count + i.getPrice()
        result = result + "TOTAL ORDER PRICE: ${:.2f}\n******\n".format(count)
        
        return result
