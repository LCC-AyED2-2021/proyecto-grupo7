from algo1 import*
from main_structures import filesList, filesNode


class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None


def InsertionSort(Q):
    amount = length(Q)
    for i in range(1, amount):
        counter = 0
        current = Q.head
        # Obtenemos el valor que vamos a comparar con los valores anteriores.
        while counter < i:
            current = current.nextNode
            counter = counter + 1
        element = current.wordReps
        fileName = current.fileName
        current = Q.head
        counter = 0
        # Comparamos el valor fijo con los valores que le preceden.
        while counter < i:
            if element > current.wordReps:
                delPosition(Q, i)
                wordReps = element
                insert(Q, fileName, counter, wordReps)
                break
            else:
                current = current.nextNode
            counter = counter + 1


def insert(L, fileName, position, wordReps):
    ''' La función insert() inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
    Entrada: la lista sobre el cual se quiere realizar la inserción Linkedlist) y el valor del elemento (element) a insertar y la posición (position) donde se quiere insertar.
    Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve None. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.
    '''
    amount = length(L)
    currentpos = 0
    current = L.head
    if position > amount:
        return None
    elif position == 0:
        add(L, fileName, wordReps)
        return position
    else:
        while current != None and currentpos < position - 1:
            current = current.nextNode
            currentpos = currentpos + 1
        if current != None:
            newNode = filesNode()
            newNode.fileName = fileName
            newNode.wordReps = wordReps
            newNode.nextNode = current.nextNode
            current.nextNode = newNode


def delPosition(L, position):
    current = L.head
    counter = 0
    if L.head == None:
        return None
    elif position == 0:
        L.head = L.head.nextNode
    else:
        while current != None:
            if counter == position - 1:
                break
            counter = counter + 1
            current = current.nextNode
        current.nextNode = current.nextNode.nextNode


def length(L):
    ''' La función length() Calcula el número de elementos de la lista que representa el TAD secuencia.
    Entrada: La lista sobre la cual se quiere calcular el número de elementos.
    Salida: Devuelve el número de elementos.
    '''
    amount = 0
    current = L.head
    while current != None:
        current = current.nextNode
        amount = amount + 1
    return amount


def add(L, fileName, wordReps):
    ''' La función add() agrega un elemento al comienzo de L, siendo L una LinkedList que representa al TAD secuencia.
    Entrada: La Lista sobre la cual se quiere agregar el elemento LinkedList) y el valor del elemento (element) a agregar.
    Salida: No hay salida definida
    '''
    newNode = filesNode()
    newNode.fileName = fileName
    newNode.wordReps = wordReps
    newNode.nextNode = L.head
    L.head = newNode
