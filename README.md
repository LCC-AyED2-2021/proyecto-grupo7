# Proyecto Algo2 - Biblioteca Virtual

DOCUMENTACIÓN:

ESTRUCTURA PRINCIPAL ELEGIDA:

En la creación del índice de términos de la biblioteca virtual, se utilizó una modificación de un árbol n-ario (Trie) como estructura principal que luego permitirá la persistencia de datos de la misma.

Dadas las siguientes clases propias del árbol n-ario (Trie) visto durante el cursado:

class Trie:
    root = None

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = None

La modificación del árbol n-ario (Trie) mencionada anteriormente consistirá en:

.       Añadir a la clase TrieNode() un campo extra, el cual se denominará 'files'.

Por lo tanto, la clase TrieNode() quedará de la siguiente manera:

class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = None
    files = None

CAMPOS

En el nuevo campo extra agregado, se guardará la siguiente información:

Una implementación modificada de la estructura LinkedList() utilizada durante el cursado. Esta modificación consiste en:

.       Crear dos nuevas clases, las cuales se denominarán de la siguiente manera:

                


FUNCIONES CREATE Y SEARCH:

En la implementación de las funciones principales create() y search() se utilizaron las siguientes estructuras





