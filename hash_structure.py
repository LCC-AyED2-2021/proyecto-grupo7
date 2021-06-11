from linkedlist import *


class nodeHash:
    key = None
    value = None
    nextNode = None


def addHashNode(L, key, value):
    newNode = nodeHash()
    newNode.key = key
    newNode.value = value
    newNode.nextNode = L.head
    L.head = newNode
    return


'''
Función hash(key):
    Recibe una key y retorna el valor hash
'''


def hash(key):
    return (key-32) % 255


def insertHash(D, value):
    if(value == None):
        return None

    posHash = hash(ord(value))

    D[posHash] = LinkedList()

    # Agrega nodo a la lista
    addHashNode(D[posHash], ord(value)-32, value)

    return D


def searchHash(D, value):
    hashList = searchHashList(D, value)
    # Si la lista no tiene nodos
    if(hashList == None or hashList.head == None):
        return None
    else:
        # Busco nodo
        hashNode = searchNodeByKey(hashList, ord(value)-32)

        # Si se encuentra el valor
        if(hashNode != None):
            return hashNode.value
        # Si no existe la key
        else:
            return None


def searchHashList(D, key):
    if(key == None):
        return None

    posHash = hash(ord(key))
    hashList = D[posHash]

    if(hashList == None):
        return None
    else:
        return hashList


def searchNodeByKey(L, key):
    if(L.head.key == key):
        return L.head

    currentNode = L.head.nextNode

    while(currentNode != None):
        # Si encuentro retorno
        if(currentNode.key == key):
            return currentNode
        currentNode = currentNode.nextNode
    return None
