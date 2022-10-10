from Book import *
from BookCollectionNode import *

class BookCollection:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
        
    def getNumberOfBooks(self):
        temp = self.head
        count = 0
        while temp != None:
            count = count + 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False
        # find the correct place in list to insert Book
        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()
        # create node with book to add
        temp = BookCollectionNode(book)

        # insert node at the front
        if previous == None:
            temp.setNext(self.head)
            self.head = temp

        # if node is not at front
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        current = self.head
        string = ""
        while current != None:
            if current.getData().getAuthor().lower() == author.lower():
                string += current.getData().getBookDetails() + "\n"
                current = current.getNext()
            else:
                current = current.getNext()
        return string
        
        
    def getAllBooksInCollection(self):
        current = self.head
        string = ''
        while current != None:
            string += current.getData().getBookDetails() + '\n'
            current = current.getNext()
        # removes end space
        return string

    def removeAuthor(self, author):
        current = self.head
        if current == None:
            return
        previous = None
        found = False
        while not found:
            if current == None:
                return
            elif current.getData().getAuthor().lower() == author.lower():
                found = True
            else:
                previous = current
                current = current.getNext()
        while current != None and current.getData().getAuthor().lower() == author.lower():
                
            current = current.getNext()
        
        # case 1 : removes 1st element
        if found == True and previous == None:
            self.head = current
        # case 2: remove not 1st element
        if found == True and previous != None:
            previous.setNext(current)

    def recursiveSearchTitle(self, title, bookNode):
        if bookNode == None:
            return False
        elif bookNode.getData().getTitle().lower() == title.lower():
            return True
        return self.recursiveSearchTitle(title, bookNode.getNext())

