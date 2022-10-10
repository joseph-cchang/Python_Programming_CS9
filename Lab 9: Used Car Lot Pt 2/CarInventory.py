# Joseph Chang, lab 09, CS9

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


    def _getSuccessor(self, currentNode):
        if not currentNode:
            return None
        elif currentNode.getRight():
            rightChild = currentNode.getRight()
            while rightChild.getLeft():
                if rightChild.getLeft() < rightChild:
                    rightChild = rightChild.getLeft()
            return rightChild

        elif not currentNode.getRight():
            parent = currentNode.getParent()
            while parent:
                if parent > currentNode:
                    return parent
                parent = parent.getParent()
                

    def getSuccessor(self, make, model):
        car_default = Car(make, model, 0, 0)
        car_node = CarInventoryNode(car_default)
        carNode = self._doesCarInventoryNodeExist(car_node, self.root)
        succ = self._getSuccessor(carNode)
        return succ
                
    def removeCar(self, make, model, year, price):
        car_default = Car(make, model, year, price)
        car_node = CarInventoryNode(car_default)
        carNode = self._doesCarInventoryNodeExist(car_node, self.root)
        
        if not carNode:
            return False
        
        for i in range(len(carNode.cars)):
            if car_default == carNode.cars[i]:
                carNode.cars.pop(i)
                break

        if len(carNode.cars) > 0:
            return True
        
        #case 1: no children (leaf)
        if not carNode.left and not carNode.right:
            if not carNode.parent:
                carNode = None
                
            elif carNode.parent.left == carNode:
                carNode.parent.left = None
            
            elif carNode.parent.right == carNode:
                carNode.parent.right = None

            
        # case 3: two children
        elif carNode.left and carNode.right:

            # case a: node to remove is leaf
            succ = self._getSuccessor(carNode)
            if not succ.left and not succ.right:
                if succ.parent and succ.parent.left == succ:
                    succ.parent.left = None
                else:
                    succ.parent.right = None

        
            # case b: Not a leaf node. Should only have a right child
            elif succ.left or succ.right:
                if succ.right:
                    if succ.parent and succ.parent.left == succ:
                        succ.parent.left = succ.right
                    else:
                        succ.parent.right = succ.right 
                    succ.right.parent = succ.parent
            carNode.cars = succ.cars         
            carNode.make = succ.make
            carNode.model = succ.model
            

        # case 2: one child
        else:
            # node has leftChild
            if carNode.left:
                if carNode.parent and carNode.parent.left == carNode:
                    carNode.left.parent = carNode.parent
                    carNode.parent.left = carNode.left
                elif carNode.parent and carNode.parent.right == carNode:
                    carNode.left.parent = carNode.parent 
                    carNode.parent.right = carNode.left
                else:
                    carNode.replaceNodeData(carNode.left.cars, carNode.left.make,
                                            carNode.left.model, carNode.left.left,
                                            carNode.left.right)

            # node has right
            else:
                if carNode.parent and carNode.parent.left == carNode:
                    carNode.right.parent = carNode.parent
                    carNode.parent.left = carNode.right
                elif carNode.parent and carNode.parent.right == carNode:
                    carNode.right.parent = carNode.parent 
                    carNode.parent.right = carNode.right
                else:
                    carNode.replaceNodeData(carNode.right.cars, carNode.right.make,
                                            carNode.right.model, carNode.right.left,
                                            carNode.right.right)

        
        return True
