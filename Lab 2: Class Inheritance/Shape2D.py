# Lab02, CS 9, Joseph Chang

# from Shape2D import Shape2D
class Shape2D:

    def __init__(self, color = None):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def getShapeProperties(self):
        return("Shape: N/A, Color: {}" \
                .format(self.color))
        
'''
s1 = Shape2D("blue")
print(s1.getShapeProperties())
'''
    
