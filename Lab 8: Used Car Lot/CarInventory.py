
from Car import *
from CarInventoryNode import *

class CarInventory():

    def __init__(self):
        self.root = None

    def _addCar(self, tempNode, currentNode):
        if tempNode == currentNode:
            currentNode.cars.append(tempNode.cars[0])

        elif tempNode < currentNode:
            if currentNode.getLeft():
                self._addCar(tempNode, currentNode.getLeft())
            else:
                currentNode.setLeft(tempNode)
                tempNode.setParent(currentNode)
                3
        else:
            if currentNode.getRight():
                self._addCar(tempNode, currentNode.getRight())
            else:
                currentNode.setRight(tempNode)
                tempNode.setParent(currentNode)
    
    def addCar(self, car):
        if self.root:
            newNode = CarInventoryNode(car)
            self._addCar(newNode, self.root)
        else:
            self.root = CarInventoryNode(car)


    def _doesCarInventoryNodeExist(self, car, currentNode):
        node = CarInventoryNode(car)
        if not currentNode:
            return None
        elif currentNode == node:
            return currentNode
        elif node < currentNode:
            return self._doesCarInventoryNodeExist(car, currentNode.getLeft())
        else:
            return self._doesCarInventoryNodeExist(car, currentNode.getRight())

    def doesCarExist(self, car):
        carNode = self._doesCarInventoryNodeExist(car, self.root)
        if carNode:
            for c in carNode.cars:
                if car == c:
                    return True
                    
        return False
            
    def inOrder(self):
        return self._inOrder(self.root)
            
    def _inOrder(self, currentNode):
        string = ''
        if currentNode:
            string = string + self._inOrder(currentNode.getLeft())
            string = string + str(currentNode)
            string = string + self._inOrder(currentNode.getRight())
        return string

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, currentNode):
        string = ''
        if currentNode:
            string = string + str(currentNode)
            string = string + self._preOrder(currentNode.getLeft())
            string = string + self._preOrder(currentNode.getRight())
        return string

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, currentNode):
        string = ''
        if currentNode:
            string = string + self._postOrder(currentNode.getLeft())
            string = string + self._postOrder(currentNode.getRight())
            string = string + str(currentNode)
        return string
    
    def getBestCar(self, make, model):
        car_default = Car(make, model, 0, 0)
        car_node = CarInventoryNode(car_default)
        carNode = self._doesCarInventoryNodeExist(car_node, self.root)

        
        if carNode:
            res = carNode.cars[0]
            for c in carNode.cars:
                if c > res:
                    res = c
            return res
        return carNode


    def getWorstCar(self, make, model):
        car_default = Car(make, model, 0, 0)
        car_node = CarInventoryNode(car_default)
        carNode = self._doesCarInventoryNodeExist(car_node, self.root)

        if carNode:
            res = carNode.cars[0]
            for c in carNode.cars:
                if c < res:
                    res = c
            return res
        return carNode
    
    
    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)

    def _getTotalInventoryPrice(self, currentNode):
        total = 0
        if currentNode:
            for c in currentNode.cars:
                total = total + c.price
            total = total + self._getTotalInventoryPrice(currentNode.getLeft())
            total = total + self._getTotalInventoryPrice(currentNode.getRight())
        return total


    
