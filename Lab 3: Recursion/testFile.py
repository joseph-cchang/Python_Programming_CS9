from lab03 import *

def test_integerDivision():
    assert integerDivision(27,4) == 6
    assert integerDivision(1,2) == 0
    assert integerDivision(31,6) == 5
    assert integerDivision(22, 2) == 11
    assert integerDivision(933, 1) == 933

def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([1, 2]) == [2]
    assert collectEvenInts([22,2334]) == [22,2334]
    assert collectEvenInts([1,3,5]) == []
    assert collectEvenInts([1]) == []

def test_countVowels():
    assert countVowels("") == 0
    assert countVowels("AaEeIiOoUu") == 10
    assert countVowels("This Is A String") == 4
    assert countVowels("SHHHHH, PSSSS, HMMMM") == 0

def test_reverseString():
    assert reverseString("CMPSC9") == "9CSPMC"
    assert reverseString("MYLOD") == "DOLYM"
    assert reverseString("") == ""
    assert reverseString("YO OY") == "YO OY"
    

def test_remove_substring():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("", "") == ""
    assert removeSubString("CS9 is good", "o") == "CS9 is gd"
    assert removeSubString("", "lol") == ""
    assert removeSubString("where is where", "where") == " is "
    
