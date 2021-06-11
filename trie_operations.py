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


def TInsert(T,element,fileName):
  ''' Descripción: inserta un elemento en T, siendo T un Trie.
  Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie), el valor del elemento (palabra)
  a agregar y el archivo en el cual se agregará.
  Salida:  No hay salida definida '''
  if T.root == None:
    T.root = TrieNode()
    T.root.key = "root"
  current = T.root
  element = String(element)
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
        add(current.children,trieNode)
        current = trieNode
      else:
        if i == len(element)-1:
          listNode.isEndOfWord = True
          currentFile = listNode.files.head
          while currentFile != None:
            if currentFile.fileName == fileName:
              reps = currentFile.wordReps
              currentFile.wordReps = reps + 1
            previousFile = currentFile  
            currentFile = currentFile.nextNode
          if currentFile == None:
            newFile = filesNode()
            newFile.fileName = fileName
            reps = newFile.wordReps
            newFile.wordReps = reps + 1
            previousFile.nextNode = newFile              
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
      add(current.children,trieNode)
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


def TSearch(T,element):
  ''' Descripción: Verifica que un elemento se encuentre dentro del Trie
  Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra).
  Salida: Devuelve False o True  según se encuentre el elemento.
  '''
  element = String(element)
  if T.root == None:
    print("El arbol ingresado no tiene raíz ni elementos dentro.")
    return False
  else:
      current = T.root.children.head
      for i in range(0,len(element)):
        while current != None and element[i] != current.value.key:
          current = current.nextNode
        if current == None:
          return False
        else:
          if i == len(element)-1 and current != None:
            if current.value != None and current.value.isEndOfWord == True:      
              return True
            else:
              return False 
          if current.value.children != None :
            current = current.value.children.head
           


def fillWord(T,newNode,i,element):
    for i in range(i,len(element)):
      newNode.value.key = element[i]
      newNode.value.children = LinkedList()
      newNode.value.children.head = Node()
      if i == len(element)-1:
        newNode.value.isEndOfWord = True
        newNode.value.children = None
        return
      parentNode = newNode            
      newNode = newNode.value.children.head                  
      newNode.value = TrieNode()
      newNode.value.parent = parentNode 
     


    
def traverseTree(T,listOfWords):
  if T.root == None or T.root.children == None:
    return None  
  word = ""
  return traverseTreeR(T.root.children,word,listOfWords)

 
def traverseTreeR(L,word,listOfWords):
  listLength = length(L)
  currentNode = L.head
  if currentNode == None:
    return
  if listLength > 1:
    while currentNode != None:
      word += currentNode.value.key
      if currentNode.value.isEndOfWord:
          add(listOfWords, word)
          if currentNode.value.children == None:
            return
      traverseTreeR(currentNode.value.children,word,listOfWords)
      word = word[:-1]
      currentNode = currentNode.nextNode
  else:
    word += currentNode.value.key
    if currentNode.value.isEndOfWord == True:
      add(listOfWords, word)
      if currentNode.value.children == None:
        return
    traverseTreeR(currentNode.value.children,word,listOfWords)
  return listOfWords  


def entireNWord(T,word,n):
  print("")
  print("Se buscan todas las palabras dentro del Trie que empiecen con la palabra", word," y que sean de longitud",n,".")
  print("")
  listOfWords = LinkedList()
  traverseTree(T, listOfWords)
  word = String(word)
  current = listOfWords.head
  while current != None:
    currentWord = String(current.value)
    for i in range(0,len(word)):
      if len(currentWord) != n:
        delete(listOfWords,current.value)
        break
      if currentWord[i] != word[i]:
        delete(listOfWords,current.value)
        break
    current = current.nextNode
  if length(listOfWords) == 0:
    print("No se encontraron palabras con las caracteristicas deseadas.")
    return False
  elif length(listOfWords) == 1:
    print("Se encontró la siguiente palabra: ",end="")
    listPrint(listOfWords)
    return True
  else:
    print("Se encontraron las siguientes palabras: ",end="")
    listPrint(listOfWords)
    return True            
      










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

