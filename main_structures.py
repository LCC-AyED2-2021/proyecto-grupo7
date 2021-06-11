from algo1 import *
from linkedlist import *


class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = None
    files = None


class filesList:
    head = None


class filesNode:
    nextNode = None
    fileName = None
    wordReps = 0


T = Trie()


def TInsert(T, element, fileName):
    ''' Descripción: inserta un elemento en T, siendo T un Trie.
    Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie), el valor del elemento (palabra)
    a agregar y el archivo en el cual se agregará.
    Salida:  No hay salida definida '''
    if T.root == None:
        T.root = TrieNode()
        T.root.key = "root"
    current = T.root

    for i in range(0, len(element)):
        if current.children != None:
            listNode = searchCharacter(current.children, element[i])
            if listNode == None:
                trieNode = TrieNode()
                trieNode.key = element[i]
                if i == len(element)-1:                    
                    trieNode.isEndOfWord = True
                    trieNode.files = filesList()
                    trieNode.files.head = filesNode()
                    currentFile = trieNode.files.head
                    currentFile.fileName = fileName
                    reps = currentFile.wordReps
                    currentFile.wordReps = reps + 1
                add(current.children, trieNode)
                current = trieNode
            else:
                if i == len(element)-1:
                    listNode.isEndOfWord = True 
                    if listNode.files == None:
                        listNode.files = filesList()
                        listAdd(listNode.files,fileName)                    
                    else:
                        currentFile = listNode.files.head
                        if currentFile.fileName == fileName:
                            currentFile.wordReps += 1
                        else:
                            listNode.files = filesList()
                            listAdd(listNode.files,fileName) 
                current = listNode
        else:
            current.children = LinkedList()
            trieNode = TrieNode()
            trieNode.parent = current
            trieNode.key = element[i]
            if i == len(element)-1:
                trieNode.isEndOfWord = True
                trieNode.files = filesList()
                trieNode.files.head = filesNode()
                currentFile = trieNode.files.head
                currentFile.fileName = fileName
                reps = currentFile.wordReps
                currentFile.wordReps = reps + 1
            add(current.children, trieNode)
            current = trieNode


def searchCharacter(L, element):
    if L == None:
        return None
    current = L.head
    while current != None:
        if current.value.key == element:
            return current.value
        current = current.nextNode
    return None


def TSearch(T, element):
    ''' Descripción: Verifica que un elemento se encuentre dentro del Trie
    Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra).
    Salida: Retorna False si el elemento no se encuentra, de lo contrario retorna una lista.
    '''
    element = String(element)
    if T.root == None:
        print("El arbol ingresado no tiene raíz ni elementos dentro.")
        return False
    else:
        current = T.root.children.head
        for i in range(0, len(element)):
            while current != None and element[i] != current.value.key:
                current = current.nextNode
            if current == None:
                return False
            else:
                if i == len(element)-1 and current != None:
                    if current.value != None and current.value.isEndOfWord == True:
                        return current.value.files
                    else:
                        return False
                if current.value.children != None:
                    current = current.value.children.head


def listAdd(list,element):
    newFile = filesNode()
    newFile.fileName = element
    newFile.wordReps = 1
    newFile.nextNode = list.head
    list.head = newFile


def listPrint(L):
  ''' La función listPrint() imprime todos los elementos de la lista enlazada. '''
  current = L.head
  while current != None:
    print(current.fileName,end = " ")
    print(current.wordReps,end = " ")
    current = current.nextNode
  print("")




# TESTEOS
# TInsert(T,"Hola","file.txt")
# print(T.root.children.head.value.children.head.value.children.head.value.children.head.value.files.head.fileName)
# print(T.root.children.head.value.children.head.value.children.head.value.children.head.value.files.head.wordReps)
# TInsert(T,"Hola","file2.txt")
# print(T.root.children.head.value.children.head.value.children.head.value.children.head.value.files.head.nextNode.fileName)
# print(T.root.children.head.value.children.head.value.children.head.value.children.head.value.files.head.nextNode.wordReps)
# TInsert(T,"Hola","file.txt")
# print(T.root.children.head.value.children.head.value.children.head.value.children.head.value.files.head.fileName)
# print(T.root.children.head.value.children.head.value.children.head.value.children.head.value.files.head.wordReps)
# TInsert(T,"hola","file.txt")
# print(T.root.children.head.value.key)


# result = TSearch(T,"Hola")

# print(result.head.fileName)
