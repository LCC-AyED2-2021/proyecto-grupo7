![Project Logo](https://i.imgur.com/OL2NjvZ.jpg)
![Python Lang Badge](https://img.shields.io/badge/-Python-f2ef3a?logo=python&logoColor=blue&style=for-the-badge) ![Project Participants](https://img.shields.io/badge/INTEGRANTES-GABRIEL%20CARRILLO%20y%20GABRIEL%20P%C3%89REZ%20DIEZ-blue?style=for-the-badge) 


### **Proyecto final de la materia 'Algoritmo y Estructuras de Datos 2' de la Universidad Nacional de Cuyo.**
El proyecto consiste la utilización de diversas estructuras de datos vistas durante el cursado, con el fin de crear un programa eficiente de busqueda de palabras en una biblioteca de archivos

# Estructuras de datos utilizadas

A continuación, se lista las estructuras utilizadas para el proyecto y se explica de qué forma se utilizan

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

En el campo files agregado, se guardará una versión modificada de Linked List (explicada en el siguiente apartado).
\
&nbsp;


### **Complejidad temporal:**
#### Inserción:


| Caso | Complejidad | 
| ---- | :---------: |
| Peor | `O(m \|Σ\|)` | 
| Promedio | `Θ(m)` |

#### Búsqueda:

| Caso | Complejidad |
| ---- | :---------: |
| Peor | `O(m \|Σ\|)` |
| Promedio | `Θ(m)` |


&nbsp;


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

### **Complejidad temporal:**
#### Búsqueda e inserción:

| Caso | Complejidad |
| ---- | :---------: |
| Promedio | `Θ(n)` |

## **Hash Tables**

Esta estructura se utilizó para verificar de forma rápida si un caractér es un símbolo especial o no.

### **Complejidad temporal:**
#### Búsqueda e inserción:

| Caso | Complejidad |
| ---- | :---------: |
| Promedio | `Θ(1)` |

# Funciones principales de la Biblioteca


## **Create**

La función ***Create*** es la encargada de separar y guardar palabras en todos los archivos de la biblioteca virtual, para luego persistir esa información y así poder usarla para la función search.

Uso:
```bash
python personal_library.py -create 'path'
```




<img src="https://i.imgur.com/YM8SPCe.gif"/>  

_Ejemplo de inserción de palabras en el Trie_


### **Complejidad temporal:**
La función tiene una complejidad promedio de `Θ(t*n*m)` siendo:
- `t`: cantidad de archivos
- `n`: cantidad de líneas en un archivo
- `m`: cantidad de caracteres por línea

&nbsp;

## **Search**

La función ***Search*** es la encargada de recuperar la información persistida por la función create, y devolver una lista de prioridades descendente con la cantidad de repeticiones de una palabra en los archivos de la biblioteca.

Uso:
```bash
python personal_library.py -search 'word'
```

### **Complejidad temporal:**
La función tiene una complejidad en el peor caso de `O(m |Σ| + n)` siendo:
- `m`: tamaño de la palabra
- `|Σ|`: tamaño del diccionario
- `n`: cantidad de archivos en

# Otros métodos y modulos utilizados

- #### **Pickle**:  módulo interno de Python, utilizado para la persistencia de objetos en archivos 
- #### **Insertion sort**: algoritmo de ordenamiento utilizado para ordernar la lista que contiene los archivos y repeticiones, obtenida en el método `-search`
- #### **Sys**: módulo interno de Python, utilizado para obtener los argumentos pasados por consola
- #### **Os**: módulo interno de Python, utilizado para acceder a los archivos en disco

