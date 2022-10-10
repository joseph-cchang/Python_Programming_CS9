# Lab 03, Joseph Chang, CS9

def integerDivision(n, k):
    if k > n:
        return 0
    else:
        return 1 + integerDivision(n-k, k)
        

def collectEvenInts(listofInt):
    if len(listofInt) == 0:
        return []
    else:
        if listofInt[0] % 2 == 0:
            return [listofInt[0]] + collectEvenInts(listofInt[1:])
        else:
            return collectEvenInts(listofInt[1:])


def countVowels(someString):
    myList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if len(someString) == 0:
        return 0
    else:
        if someString[0] in myList:
            return 1 + countVowels(someString[1:])
        else:
            return countVowels(someString[1:])


def reverseString(s):
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s
    else:
        return reverseString(s[1:]) + s[0] 
    


def removeSubString(s, sub):
    if len(s) == 0:
        return ""
    else:
        if s[0:len(sub)] == sub:
            return removeSubString(s[len(sub):], sub)
        else:
            return s[0] + removeSubString(s[1:], sub)


