# Lab01, CS 9, Joseph Chang

from Animal import Animal
class AnimalShelter:

    ''' This is the AnimalShelter class
    '''

    def __init__(self):
        self.animalshelter = {}

    def addAnimal(self, animal):
        # if animalshelter does not exist
        
        if self.animalshelter.get(animal.species) == None:
            self.animalshelter[animal.species] = [animal]
        elif not animal in self.animalshelter.get(animal.species):
            self.animalshelter[animal.species].append(animal)


    def removeAnimal(self, animal):
        # if animalshelter does exist
        
        if self.animalshelter.get(animal.species) != None:
            for idx, i in enumerate(self.animalshelter[animal.species]):
                if i.name == animal.name and i.age == animal.age and i.weight == animal.weight:
                    self.animalshelter[animal.species].pop(idx)
        

    def removeSpecies(self, species):
        # remove specifc entry of species in dictionary

        myspecies = species.upper()
        
        # if animalshelter exists
        if self.animalshelter.get(myspecies) != None:
            self.animalshelter.pop(myspecies)


    def getAnimalsBySpecies(self, species):

        myspecies = species.upper()
       
        mystring = ""
        if self.animalshelter.get(myspecies) == None:
            return ""
        else: 
            for i in self.animalshelter[myspecies]:
                if i == self.animalshelter[myspecies][-1]:
                    mystring = mystring + i.toString() 
                else:
                    mystring = mystring + i.toString() + '\n'
            return mystring
         
    #    last animal in list should not have new line
    #    remove last character
    

    def doesAnimalExist(self, animal):
        if animal.species in self.animalshelter:
            for idx, i in enumerate(self.animalshelter[animal.species]):
                if i.name == animal.name and i.age == animal.age and i.weight == animal.weight:
                    return True
                else:
                    return False
            return False
        else:
            return False


