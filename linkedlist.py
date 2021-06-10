from algo1 import *

# EJERCITACIÓN TAD LISTA

class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

L = LinkedList()



def add(L,element):
  ''' La función add() agrega un elemento al comienzo de L, siendo L una LinkedList que representa al TAD secuencia.
  Entrada: La Lista sobre la cual se quiere agregar el elemento LinkedList) y el valor del elemento (element) a agregar.
  Salida: No hay salida definida
  '''
  newNode = Node()
  newNode.value = element
  newNode.nextNode = L.head
  L.head = newNode
  return 0



def search(L,element):
  ''' La función search() busca un elemento de la lista que representa el TAD secuencia.
  Entrada: La Lista sobre la cual se quiere agregar el elemento LinkedList) y el valor del elemento (element) a agregar.
  Salida: Devuelve la posición donde se encuentra la primera instancia del elemento. Devuelve None si el elemento no se encuentra.
  '''
  current = L.head
  amount = 0
  while current != None:
    if current.value == element:
      return amount
    current = current.nextNode
    amount = amount + 1
  return None    



def insert(L,element,position):
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
    add(L,element)
    return position
  else:
    while current != None and currentpos < position - 1:
      current = current.nextNode
      currentpos = currentpos + 1
    if current != None:
      newNode = Node()
      newNode.value = element
      newNode.nextNode = current.nextNode
      current.nextNode = newNode 
      if access(L,position) == element:
        return position 
      else:
        return None  



def delete(L,element):
  ''' La función delete() elimina un elemento de la lista que representa el TAD secuencia.
  Poscondición: Se debe desvincular el Node a eliminar.
  Entrada: la lista sobre el cual se quiere realizar la eliminación Linkedlist) y el valor del elemento (element) a eliminar.
  Salida: Devuelve la posición donde se encuentra el elemento a eliminar. Devuelve None si el elemento a eliminar no se encuentra.
  '''  
  current = L.head
  position = search(L,element)
  if position == 0:
    L.head = current.nextNode
    return position 
  elif position != None:
    for i in range(0,position - 1):
     current = current.nextNode 
    current.nextNode = current.nextNode.nextNode 
    return position   
  else:
    return None



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



def access(L,position):
  ''' La función access() permite acceder a un elemento de la lista en una posición determinada.
  Entrada: La lista (LinkedList) y la position del elemento al cual se quiere acceder.
  Salida: Devuelve el valor de un elemento en una position de la lista,devuelve None si no existe elemento para dicha posición.
  '''
  element = None
  current = L.head
  counter = 0
  while current != None:
    if counter == position:
      element = current.value
      break
    counter = counter + 1
    current = current.nextNode

  return element 



def update(L,element,position):
  ''' La función update() permite cambiar el valor de un elemento de la lista en una posición determinada
  Entrada: La lista (LinkedList) y la position sobre la cual se quiere asignar el valor de element.
  Salida: Devuelve None si no existe elemento para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.
  '''
  current = L.head
  posicion = None
  counter = 0
  if access(L,position) != None:
    while current != None:
      if counter == position:
        current.value = element
        posicion = position
        break
      counter = counter + 1
      current = current.nextNode


def enqueue(Q,element):
	insert(Q,element,length(Q))

def dequeue(Q):
  if length(Q) == None:
    element = None
  else:
    element = (access(Q, 0))
    delete(Q,access(Q, 0))
  return element

def push(S,element):
  add(S,element)
  return

def pop(S):

  element = None
  if S.head != None:
    element = access(S,0)
    delete(S,access(S,0))

  return element

def move(L,position_orig,position_dest):
  element = access(L,position_orig)
  delPosition(L,position_orig)
  insert(L,element,position_dest)

  
def delPosition(L,position): 
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


def BubbleSort(L):
  amount = length(L)
  counter = 0
  current = L.head
  while counter <= amount:
    current = L.head
    for i in range(0,amount - 1 - counter):
      if current.value > current.nextNode.value:
        element = current.value
        current.value = current.nextNode.value
        current.nextNode.value = element
      current = current.nextNode       
    counter = counter + 1  

def SelectionSort(S):
  amount = length(S)
  counter = 0
  current = S.head
  # Buscamos el menor número de la lista.
  while counter <= amount - 1:
    element = None
    current = S.head
    if counter != 0:
      position = 0
      while position < counter:
        current = current.nextNode
        position = position + 1    
    if current != None:
      minor = current.value
    change = False
    for i in range(counter,amount):
      if current.value < minor:
        change = True
        minor = current.value
        location = i
      current = current.nextNode
    element = access(S,counter)
    update(S,minor,counter)
    if change == True:
      update(S,element,location)
    counter = counter + 1

def InsertionSort(Q):
  amount = length(Q)
  for i in range(1,amount):
    counter = 0
    current = Q.head
    # Obtenemos el valor que vamos a comparar con los valores anteriores.
    while counter < i:
      current = current.nextNode
      counter = counter + 1
    element = current.value
    current = Q.head
    counter = 0
    # Comparamos el valor fijo con los valores que le preceden.
    while counter < i:
      if element < current.value:
        delPosition(Q,i)
        insert(Q,element,counter)
        break
      else:  
        current = current.nextNode
      counter = counter + 1 

def listPrint(L):
  ''' La función listPrint() imprime todos los elementos de la lista enlazada. '''
  current = L.head
  while current != None:
    print(current.value,end = " ")
    current = current.nextNode
  print("")
