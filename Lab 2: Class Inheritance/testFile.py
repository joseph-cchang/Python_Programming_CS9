
from Shape2D import Shape2D
from Circle import Circle
from Square import Square


def test_Shape2D():

    # check if any other color works
    test1 = Shape2D("orange")
    assert test1.getShapeProperties() == "Shape: N/A, Color: orange"

    # check if color in caps works
    test2 = Shape2D("RED")
    assert test2.getShapeProperties() == "Shape: N/A, Color: RED"

    # testing setter/getter method
    test3 = Shape2D("blue")
    test3.setColor("blue")
    assert test3.getColor() == "blue"
        

def test_circle():

    c1 = Circle("blue", 2.5)
    assert c1.getShapeProperties() == "Shape: CIRCLE, Color: blue, Radius: 2.5, Area: 19.6349375, Perimeter: 15.70795"

    c2 = Circle("red", 1)
    c2.setRadius(1)
    assert c2.getRadius() == 1
    assert c2.computeArea() == 3.14159
    assert c2.computePerimeter() == 6.28318


def test_Square():
    
    s1 = Square("green", 0)
    s1.setSide(0)
    
    assert s1.getSide() == 0
    assert s1.computeArea() == 0
    assert s1.computePerimeter() == 0

    assert s1.getShapeProperties() == "Shape: SQUARE, Color: green, Side: 0, Area: 0, Perimeter: 0"




