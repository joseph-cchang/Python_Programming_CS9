# Joseph Chang, Lab 09, CS 9

from Car import *

class CarInventoryNode:

    def __init__(self, car):
        
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.left = None
        self.right = None
        self.parent = None
        self.cars = [car]

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent 
    
    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left 

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        s = ''
        for i in self.cars:
            s += str(i) + "\n"
            
        return s

    def replaceNodeData(self, cars, make, model, left, right):
        self.cars = cars
        self.make = make
        self.model = model
        self.left = left
        self.right = right

        if self.left:
            self.left.parent = self

        if self.right:
            self.right.parent = self

        
    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make < rhs.make:
            return False
        else:
            if self.model > rhs.model:
                return True
            elif self.model < rhs.model:
                return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make > rhs.make:
            return False
        else:
            if self.model < rhs.model:
                return True
            elif self.model > rhs.model:
                return False
        
    def __eq__(self, rhs):
        if rhs == None:
            return False
        elif self.make == rhs.make and self.model == rhs.model:
            return True




