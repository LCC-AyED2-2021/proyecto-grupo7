from algo1 import *


def createImportantCharHash():
    hashTable = Array(24, "")
    insertHash(hashTable, " ")
    insertHash(hashTable, "\t")
    insertHash(hashTable, "\n")
    return hashTable


def createWordsTable():
    hashTable = Array(247, "")
    insertHash(hashTable, "A")
    insertHash(hashTable, "Á")
    insertHash(hashTable, "a")
    insertHash(hashTable, "á")
    insertHash(hashTable, "B")
    insertHash(hashTable, "b")
    insertHash(hashTable, "C")
    insertHash(hashTable, "c")
    insertHash(hashTable, "D")
    insertHash(hashTable, "d")
    insertHash(hashTable, "E")
    insertHash(hashTable, "É")
    insertHash(hashTable, "e")
    insertHash(hashTable, "é")
    insertHash(hashTable, "F")
    insertHash(hashTable, "f")
    insertHash(hashTable, "G")
    insertHash(hashTable, "g")
    insertHash(hashTable, "H")
    insertHash(hashTable, "h")
    insertHash(hashTable, "I")
    insertHash(hashTable, "Í")
    insertHash(hashTable, "i")
    insertHash(hashTable, "í")
    insertHash(hashTable, "J")
    insertHash(hashTable, "j")
    insertHash(hashTable, "K")
    insertHash(hashTable, "k")
    insertHash(hashTable, "L")
    insertHash(hashTable, "l")
    insertHash(hashTable, "M")
    insertHash(hashTable, "m")
    insertHash(hashTable, "N")
    insertHash(hashTable, "n")
    insertHash(hashTable, "Ñ")
    insertHash(hashTable, "ñ")
    insertHash(hashTable, "O")
    insertHash(hashTable, "Ó")
    insertHash(hashTable, "o")
    insertHash(hashTable, "ó")
    insertHash(hashTable, "P")
    insertHash(hashTable, "p")
    insertHash(hashTable, "Q")
    insertHash(hashTable, "q")
    insertHash(hashTable, "R")
    insertHash(hashTable, "r")
    insertHash(hashTable, "S")
    insertHash(hashTable, "s")
    insertHash(hashTable, "T")
    insertHash(hashTable, "t")
    insertHash(hashTable, "U")
    insertHash(hashTable, "Ú")
    insertHash(hashTable, "u")
    insertHash(hashTable, "ú")
    insertHash(hashTable, "V")
    insertHash(hashTable, "v")
    insertHash(hashTable, "W")
    insertHash(hashTable, "w")
    insertHash(hashTable, "X")
    insertHash(hashTable, "x")
    insertHash(hashTable, "Y")
    insertHash(hashTable, "y")
    insertHash(hashTable, "Z")
    insertHash(hashTable, "z")
    insertHash(hashTable, "0")
    insertHash(hashTable, "1")
    insertHash(hashTable, "2")
    insertHash(hashTable, "3")
    insertHash(hashTable, "4")
    insertHash(hashTable, "5")
    insertHash(hashTable, "6")
    insertHash(hashTable, "7")
    insertHash(hashTable, "8")
    insertHash(hashTable, "9")
    return hashTable


def hash(key):
    return ord(key)-9


def insertHash(D, value):
    if(value == None):
        return None

    posHash = hash(value)
    D[posHash] = value

    # return D
    return posHash


def searchHash(D, value):
    posHash = hash(value)
    if(posHash > 246 or posHash < 39):
        return None
    if(D[posHash] == value):
        return value
    return None


def specialSearchHash(D, value):
    posHash = hash(value)
    if(posHash < 0 or posHash > 23):
        return None
    if(D[posHash] == value):
        return value
    return None
