# Lab01, CS 9, Joseph Chang

class Animal:
    ''' This function is the Animal class.

    '''

    def __init__(self, species= None, weight = None, age = None, name= None):
        self.species = species
        if self.species != None:
            self.species = species.upper()
        self.weight = weight
        self.age = age
        self.name = name
        if self.name != None:
            self.name = name.upper()
        
    # setters
    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

        
    # getter(s)
    def toString(self):
        return ("Species: {}, Name: {}, Age: {}, Weight: {}"\
             .format(self.species, self.name, self.age, self.weight))
        
'''
a = Animal(species = "Dog", name= "doggy", age= 4, weight = 23.6)
print(a.toString())
''' 

