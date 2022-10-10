# Lab02, CS 9, Joseph Chang

from Shape2D import Shape2D
class Circle(Shape2D):
    def __init__(self, color = None, radius = None):
        super().__init__(color)
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def computeArea(self):
        return 3.14159 * self.radius ** 2

    def computePerimeter(self):
        return 3.14159*2*self.radius


    def getShapeProperties(self):
        return ("Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}" \
             .format(self.color, self.getRadius(), self.computeArea(), self.computePerimeter()))

'''
c1 = Circle("blue", 2.5)
print(c1.getShapeProperties())
'''    
    
