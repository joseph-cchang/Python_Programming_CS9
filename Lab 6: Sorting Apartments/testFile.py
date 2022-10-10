# testFile

from Apartment import *
from lab06 import *

def test_equals():
    a = Apartment(1204, 200, "average")
    b = Apartment(1204, 200, "average")
    assert a==b
    

def test_gt():
    a = Apartment(1204, 200, "bad")
    b = Apartment(1204, 200, "average")
    assert a>b

    c = Apartment(300, 300, "bad")
    d = Apartment(200, 300, "excellent")
    assert c>d

    e = Apartment(0, 400, "excellent")
    f = Apartment(0, 200, "average")
    assert e > f

def test_lt():
    a = Apartment(1204, 200, "excellent")
    b = Apartment(1204, 200, "average")
    assert a < b

    c = Apartment(3000, 0, "average")
    d = Apartment(5000, 0, "average")
    assert c < d

    e = Apartment(50, 400, "excellent")
    f = Apartment(50, 600, "excellent")
    assert e < f
 
def test_ensureSortedAscending():

    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]


    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_ensureSortedAscending2():

    a0 = Apartment(1115, 215, "bad")
    apartmentList = [a0]
    assert ensureSortedAscending(apartmentList) == True
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True


def test_get_Best_Apartment():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "good")
    a5 = Apartment(700, 315, "bad")
    a6 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5, a6]

    assert ensureSortedAscending(apartmentList) == False

    assert getBestApartment(apartmentList) == \
           "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: good"


def test_get_Best_Apartment2():
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a5]

    assert getBestApartment(apartmentList) == \
           "(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"


def test_get_Worst_Apartment():
    
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getWorstApartment(apartmentList) == \
           "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"

def test_get_Worst_Apartment2():
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a5]

    assert getWorstApartment(apartmentList) == \
           "(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"



def test_get_Affordable_Apartments():
    
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    
    assert getAffordableApartments(apartmentList, 950) == \
           "(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad\n\
(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent\n\
(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average"


def test_get_Affordable_Apartments2():
    
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(900, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getAffordableApartments(apartmentList, 800) == ""


