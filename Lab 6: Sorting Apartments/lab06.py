# lab06

from Apartment import *

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
    
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1 
            k = k + 1
    
def ensureSortedAscending(apartmentList):
    for apartment in range(len(apartmentList)-1):
        if apartmentList[apartment] > apartmentList[apartment+1]:
            return False
    return True

  
def getBestApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[0].getApartmentDetails()

        
def getWorstApartment(apartmentList):
    mergesort(apartmentList)
    return apartmentList[len(apartmentList)-1].getApartmentDetails()


def getAffordableApartments(apartmentList, budget):
    string = ""
    mergesort(apartmentList)
    for apartment in range(len(apartmentList)):
        if apartmentList[apartment].getRent() <= budget:
            string += apartmentList[apartment].getApartmentDetails() + "\n"
    return string[:-1]



