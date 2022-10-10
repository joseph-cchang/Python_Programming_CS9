# testFile

from Car import *
from CarInventoryNode import *
from CarInventory import *

def test_car():
    c = Car("Honda", "CRV", 2007, 8000)
    assert str(c) == "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"

def test_gt():
    a = Car("Toyota", "Camry", 2007, 8000)
    b = Car("Toyota", "Prius", 2007, 8000)
    assert b > a

    c = Car("Ford", "Focus", 2007, 8000)
    d = Car("Toyota", "Prius", 2007, 8000)
    assert d > c

    e = Car("Toyota", "Prius", 1000, 8000)
    f = Car("Toyota", "Prius", 2007, 8000)
    assert f > e

    g = Car("Toyota", "Prius", 2007, 5000)
    h = Car("Toyota", "Prius", 2007, 8000)
    assert h > g


def test_lt():
    a = Car("Toyota", "Prius", 2007, 5000)
    b = Car("Toyota", "Camry", 2007, 5000)
    assert b < a

    c = Car("Toyota", "Prius", 2007, 8000)
    d = Car("Ford", "Focus", 2007, 8000)
    assert d < c

    e = Car("Toyota", "Prius", 3000, 8000)
    f = Car("Toyota", "Prius", 2007, 8000)
    assert f < e

    g = Car("Toyota", "Prius", 2007, 9000)
    h = Car("Toyota", "Prius", 2007, 8000)
    assert h < g


def test_eq():
    a = Car("Toyota", "Camry", 2007, 5000)
    b = Car("Toyota", "Camry", 2007, 5000)
    assert b == a

    e = Car("Toyota", "Camry", 2007, 5000)
    f = Car("Toyota", "Camry", 2007, 3000)
    assert e != f


def test_carInventoryNode():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)

    assert str(carNode) ==\
    "Make: DODGE, Model: DART, Year: 2015, Price: $6000\n\
Make: DODGE, Model: DART, Year: 2003, Price: $5000\n"


    car3 = Car("Ford", "ford", 1901, 3000)
    carNode2 = CarInventoryNode(car3)

    assert str(carNode2) ==\
    "Make: FORD, Model: FORD, Year: 1901, Price: $3000\n"


    
# testing for CarInventory Part 1

bst = CarInventory()

car1 = Car("Nissan", "Leaf", 2018, 18000)
car2 = Car("Tesla", "Model3", 2018, 50000)
car3 = Car("Mercedes", "Sprinter", 2022, 40000)
car4 = Car("Mercedes", "Sprinter", 2014, 25000)
car5 = Car("Ford", "Ranger", 2021, 25000)

bst.addCar(car1)
bst.addCar(car2)
bst.addCar(car3)
bst.addCar(car4)
bst.addCar(car5)


def test_carInventory_doesCarExist():
    assert bst.doesCarExist(car5) == True
    
def test_inOrder_preOrder_postOrder():

    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""

    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""


    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""



def test_bestCar_worstCar_Inventory_Price():

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getTotalInventoryPrice() == 158000


# testing for carInventory Part2

bst2 = CarInventory()

my_car = Car("Toyota", "Camry", 2007, 30000)
my_car2 = Car("Test", "test", 0, 0)
bst2.addCar(my_car)

def test_carInventory_doesCarExist2():
    assert bst2.doesCarExist(my_car) == True
    assert bst2.doesCarExist(my_car2) == False

def test2_inOrder_preOrder_postOrder():

    assert bst2.inOrder() == \
"""\
Make: TOYOTA, Model: CAMRY, Year: 2007, Price: $30000
"""

    assert bst2.preOrder() == \
"""\
Make: TOYOTA, Model: CAMRY, Year: 2007, Price: $30000
"""

    assert bst2.postOrder() == \
"""\
Make: TOYOTA, Model: CAMRY, Year: 2007, Price: $30000
"""


def test2_bestCar_worstCar_Inventory_Price():

    assert bst2.getBestCar("Toyota", "Camry") == my_car

    assert bst2.getWorstCar("Toyota", "Camry") == my_car

    assert bst2.getTotalInventoryPrice() == 30000

def test_successor():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)


    assert bst.getSuccessor("Audi", "A3").make == "BMW"
    assert bst.getSuccessor("Audi", "A3").model == "X5"

    assert bst.getSuccessor("Mazda", "CX-5").make == "TESLA"
    assert bst.getSuccessor("Mazda", "CX-5").model == "MODEL3"
    


def test_remove_leaf_child_and_one_left_child_inOrder():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    # removes leaf child
    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""

    # removes node with one child
    bst.removeCar("BMW", "X5", 2022, 60000)

    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""

def test_remove_leaf_child_and_one_left_child_preOrder():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)
    
    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""

    bst.removeCar("BMW", "X5", 2022, 60000)


    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""


def test_remove_leaf_child_and_one_left_child_postOrder():
    bst = CarInventory()

    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2020, 58000)

    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
"""

    bst.removeCar("BMW", "X5", 2022, 60000)


    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
"""

def test_remove_one_right_child():

    bst = CarInventory()
    
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("BMW", "X5", 2022, 60000)
    
    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: BMW, Model: X5, Year: 2020, Price: $58000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""

    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: BMW, Model: X5, Year: 2020, Price: $58000\n\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""

    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: BMW, Model: X5, Year: 2020, Price: $58000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
"""

def test_remove_two_children():

    bst = CarInventory()
    
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car6 = Car("Joseph", "Chang", 2000, 0)
    car3 = Car("BMW", "X5", 2022, 60000)
    car4 = Car("BMW", "X5", 2020, 58000)
    car5 = Car("Audi", "A3", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car6)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    bst.removeCar("Joseph", "Chang", 2000, 0)

    assert bst.inOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: BMW, Model: X5, Year: 2020, Price: $58000\n\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""
    
    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: BMW, Model: X5, Year: 2022, Price: $60000\n\
Make: BMW, Model: X5, Year: 2020, Price: $58000\n\
Make: AUDI, Model: A3, Year: 2021, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
"""

    assert bst.postOrder() == \
"""\
Make: AUDI, Model: A3, Year: 2021, Price: $25000
Make: BMW, Model: X5, Year: 2022, Price: $60000
Make: BMW, Model: X5, Year: 2020, Price: $58000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000
"""

def test_remove_root_node():
    
    bst = CarInventory()
    car6 = Car("Joseph", "Chang", 2000, 0)
    bst.addCar(car6)

    bst.removeCar("Joseph", "Chang", 2000, 0)

    assert bst.preOrder() == \
"""\
"""

def test_remove_node_with_one_child():

    bst = CarInventory()
    
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Volvo", "Good", 2000, 2000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)

    bst.removeCar("Tesla", "Model3", 2018, 50000)

    assert bst.inOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: VOLVO, Model: GOOD, Year: 2000, Price: $2000\n\
"""

def test_doesCarExist():

    bst = CarInventory()
    
    car1 = Car("Mazda", "CX-5", 2022, 25000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Volvo", "Good", 2000, 2000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)

    bst.removeCar("Tesla", "Model1", 0, 0)

    assert bst.preOrder() == \
"""\
Make: MAZDA, Model: CX-5, Year: 2022, Price: $25000\n\
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n\
Make: VOLVO, Model: GOOD, Year: 2000, Price: $2000\n\
"""


