# Lab02, CS 9, Joseph Chang

from Shape2D import Shape2D
class Square(Shape2D):

    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        return self.side * self.side

    def computePerimeter(self):
        return self.side * 4

    def getShapeProperties(self):
        return ("Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}" \
             .format(self.color, self.side, self.computeArea(), self.computePerimeter()))
        
    
'''
s1 = Square("blue", 2.5)
print(s1.getShapeProperties())
'''
