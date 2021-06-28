![logo](https://i.imgur.com/OL2NjvZ.jpg)
![integrantes](https://img.shields.io/badge/INTEGRANTES-GABRIEL%20P%C3%89REZ%20DIEZ%20%20y%20GABRIEL%20CARRILLO-blue?style=for-the-badge) ![lenguaje](https://img.shields.io/badge/-Python-f2ef3a?logo=python&logoColor=blue&style=for-the-badge)


Proyecto final de la materia 'Algoritmo y Estructuras de Datos 2' de la Universidad Nacional de Cuyo.
El proyecto consiste la utilización de diversas estructuras de datos vistas durante el cursado, con el fin de crear un programa eficiente de busqueda de palabras en una biblioteca de archivos

# Estructuras de datos utilizadas

## **Trie** (Estructura Principal)

Como estructura principal para el almacenamiento de datos de la biblioteca virtual, se eligió la estructura Trie (o árbol n-ario).

La elección se fundamenta en base a la optimización del espacio requerido en memoria, en lo que Trie resulta una buena opción ya que permite minimizarlo.

Dadas las siguientes clases propias del árbol n-ario (Trie) vistas durante el cursado:

* Trie
* TrieNode

Se utilizó una modificación de un árbol n-ario (Trie) cuyo cambio es el siguiente:

* Se añadió a la clase TrieNode() un campo extra, el cual se denomina 'files'.

Por lo que la clase TrieNode() modificada queda de la siguiente manera:

``` python
class TrieNode:
    parent = None # nodo padre
    children = None # lista con nodos hijos
    key = None # caracter
    isEndOfWord = None # indicador fin de palabra
    files = None # campo nuevo
```

En el campo files agregado, se guardará una versión modificada de Linked List.

## **Linked List**

Se utilizó una versión modificada de Linked List, la cual esta re-definida de la siguiente manera:

``` python
class filesList:
    head = None # primer nodo de la lista

class filesNode:
    nextNode = None # siguiente nodo de la lista
    fileName = None # nombre del archivo
    wordReps = 0 # cantidad de repeticiones
```

Esta estructura, utilizada en el campo files de la clase TrieNode, contiene la cantidad de repeticiones de cada palabra por archivo.

## **Hash Tables**

Se utilizó la estructura de Hash Table

# Funciones principales de la Biblioteca


## **Create**

<img src="https://i.imgur.com/cU9fi3p.gif" style="width: 40%; height: 40%"/>

> Ejemplo de inserción de palabras en el Trie

## **Search**

# Persistencia de Datos



<!-- ``` python
class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = None
``` -->
<!-- La modificación del árbol n-ario (Trie) mencionada anteriormente consistirá en: -->
