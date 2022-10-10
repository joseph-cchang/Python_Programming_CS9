# TestFile

from Book import *
from BookCollection import *
from BookCollectionNode import *

# test getbookDetails
def test_getBookDetails():
    b = Book("Ready Player One", "Cline, Ernest", 2011)
    assert b.getBookDetails() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011"

# test if a book comes before another book in list
def test_gt_():
    a = Book("All about me", "Chang, Joseph", 2022)
    b = Book("All about me2", "Chang, Joseph", 2021)
    assert (a > b) == True

# method for testing getData and getNext
def test_getData():
    n = BookCollectionNode(20)
    assert n.getData() == 20
    assert n.getNext() == None

# method to test setData
def test_setData():
    n = BookCollectionNode(20)
    n.setData(200)
    assert n.getData() == 200

# method to test setNext
def test_setNext():
    n = BookCollectionNode(10)
    n2 = BookCollectionNode(20)
    n.setNext(n2)
    assert n.getNext() == n2

def test_isEmpty():
    bc = BookCollection()
    assert bc.isEmpty() == True

def test_getNumberOfBooks():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    assert bc.getNumberOfBooks() == 3

def test_getBooksByAuthor():
    
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getBooksByAuthor("KING, Stephen") == "Title: Rage, Author: King, Stephen, Year: 1977\n\
Title: The Shining, Author: King, Stephen, Year: 1977\n\
Title: Cujo, Author: King, Stephen, Year: 1981\n"


def test_getBooksByAuthor2():
    b0 = Book("Title", "A, A", 0)
    bc = BookCollection()
    bc.insertBook(b0)
    assert bc.getBooksByAuthor("A, A") == "Title: Title, Author: A, A, Year: 0\n"


def test_getAllBooksCollection():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n\
Title: Rage, Author: King, Stephen, Year: 1977\n\
Title: The Shining, Author: King, Stephen, Year: 1977\n\
Title: Cujo, Author: King, Stephen, Year: 1981\n"

def test_getAllBooksCollection2():
    b0 = Book("Title", "A, A", 0)
    bc = BookCollection()
    bc.insertBook(b0)
    assert bc.getAllBooksInCollection() == "Title: Title, Author: A, A, Year: 0\n"


def test_remove_author():

    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)

    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    bc.removeAuthor("King, Stephen")
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n" 


def test_remove_author2():
    b0 = Book("Title", "A, A", 0)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.removeAuthor("A, A")
    assert bc.getAllBooksInCollection() == ""



def test_recursiveSearchTitle():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("CUJO", bc.head) == True
    assert bc.recursiveSearchTitle("Twilight", bc.head) == False


def test_recursiveSearchTitle2():
    b0 = Book("Me", "Chang, Joseph", 2021)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Me2", "Chang, Joseph", 2022)
    bc = BookCollection()
    bc.insertBook(b0)
    bc.insertBook(b1)
    assert bc.recursiveSearchTitle("Me", bc.head) == True
    assert bc.recursiveSearchTitle("Me3", bc.head) == False

