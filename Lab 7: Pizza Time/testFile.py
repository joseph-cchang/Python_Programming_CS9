# testFile

from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *
from PizzaOrder import *
from OrderQueue import *


def test_getPizza():
    cp1 = CustomPizza("S")
    cp1.setPrice(8.00)
    assert cp1.getPrice() == 8.00

def test_():
    cp1 = CustomPizza("S")

    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"

def test_Custom_Pizza():
    cp1 = CustomPizza("S")

    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\n\
Price: $8.00\n"

    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")

    assert cp1.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\n\
\t+ extra cheese\n\t+ sausage\nPrice: $14.00\n"
    




def test_Specialty_Pizza():
    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == "SPECIALTY PIZZA\nSize: S\n\
Name: Carne-more\nPrice: $12.00\n"





def test_pizza_order():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"





def test_pizza_order2():
    cp1 = CustomPizza("L")
    sp1 = SpecialtyPizza("L", "Joseph")
    order = PizzaOrder(10000)
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 10000\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: Joseph\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $28.00\n\
******\n"




def test_add_order_orderQueue():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")

    order = PizzaOrder(123000) #12:30:00PM

    order.addPizza(cp1)
    order.addPizza(sp1)

    queue1 = OrderQueue()
    queue1.addOrder(order)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"



def test_processNextOrder():
    cp1 = CustomPizza("S")
    sp1 = SpecialtyPizza("S", "Carne-more")
    cp2 = CustomPizza("L")
    sp2 = SpecialtyPizza("L", "Joseph")

    order = PizzaOrder(100000) #10:00:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    order2 = PizzaOrder(110000)
    order2.addPizza(cp2)
    order2.addPizza(sp2)

    queue1 = OrderQueue()
    queue1.addOrder(order)
    queue1.addOrder(order2)

    assert order.getOrderDescription() == \
"******\n\
Order Time: 100000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $20.00\n\
******\n"

    assert queue1.processNextOrder() == \
"******\n\
Order Time: 100000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $20.00\n\
******\n"

    assert queue1.processNextOrder() == \
"******\n\
Order Time: 110000\n\
CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
Price: $12.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: L\n\
Name: Joseph\n\
Price: $16.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $28.00\n\
******\n"
    

'''
def test_EmptyQueue():
    queue1 = OrderQueue()
    with pytest.raises(QueueEmptyException):
        heap = OrderQueue()
        heap.processNextOrder() # this line would raise the QueueEmptyException

'''


    
