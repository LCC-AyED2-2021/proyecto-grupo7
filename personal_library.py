# Imports manipulación de archivos
import sys
import os

# Import para serialización de datos
import pickle

# Imports propios
from algo1 import *
from main_structures import *
from hash_structure import *
from insertionsort_structure import InsertionSort


# Para que no haya errores con Pickle
sys.setrecursionlimit(10000)


'''
Función isTextFile(filename)
    Verifica si un archivo tiene extensión .txt
'''


def isTextFile(filename):
    filenameLength = len(filename)
    # Si la longitud del filename es menor a 5, no tiene extensión txt
    if(filenameLength < 5):
        return False

    # String para comparar
    txtExtension = String(".txt")

    count = 0

    # Verifico que los últimos 4 caracteres sean '.txt'
    for i in range(filenameLength - 4, filenameLength):
        # Si no matchean con el string de comparación, es otra extensión
        if(filename[i] != txtExtension[count]):
            return False
        count += 1
    return True


'''
Función create
    Lógica central del programa, recorre archivos, extrae las palabras y las serializa
'''


def create(path):
    # Arreglo con los archivos del directorio
    libraryFiles = os.listdir(path)
    amountFiles = len(libraryFiles)

    # Si no hay archivos en la biblioteca
    if(amountFiles == 0):
        print("No hay archivos en la biblioteca")
        return
    print("Creando la biblioteca..")

    # Creo Trie
    wordsTree = Trie()

    # Tabla hash de caracteres normales
    wordsTable = createWordsTable()
    # Tabla hash de caracteres especiales
    importantCharHash = createImportantCharHash()

    # Recorro los archivos del directorio
    for file in libraryFiles:
        # Solo leo archivo si es TXT
        if(isTextFile(file)):
            with open(path + "/" + file, 'r', encoding='utf-8') as currentFile:

                fileLines = currentFile.readlines()

                # Por cada linea del archivo..
                for line in fileLines:
                    # Convierto a String✨ de Algo 1
                    line = String(line)
                    lineLength = len(line)
                    word = String("")

                    # Por cada caracter de la línea..
                    for i in range(0, lineLength):

                        # Si el caracter NO es un símbolo especial
                        if(searchHash(wordsTable, line[i])):

                            # Concateno en la palabra
                            word = concat(word, String(line[i]))

                            # Si es el final de la línea..
                            if(i == lineLength-1):
                                # Inserto la palabra en el Trie
                                TInsert(wordsTree, word, file)
                                word = String("")

                        # Si el caracter en cambio ES un símbolo especial
                        else:
                            # Si todavía la palabra no tiene caracteres, ignoro el símbolo
                            if(len(word) >= 1):
                                # Si es un caracter especial y estamos al final de la linea
                                if(i == lineLength-1 or i+1 == lineLength-1):
                                    # Inserto la palabra en el Trie
                                    TInsert(wordsTree, word, file)
                                    word = String("")
                                else:
                                    # Si los caracteres que siguen (2 posiciones más adelante) o el actual, es un salto de linea, espacio o tab
                                    if(specialSearchHash(importantCharHash, line[i]) != None or specialSearchHash(importantCharHash, line[i+1]) != None or specialSearchHash(importantCharHash, line[i+2]) != None):
                                        # Inserto la palabra en el Trie e ignoro
                                        TInsert(wordsTree, word, file)
                                        word = String("")
                                    else:
                                        # Si no, concateno a la palabra
                                        word = concat(word, String(line[i]))
    # Guardo trie en pickle
    with open('library.bin', 'bw') as lib:
        pickle.dump(wordsTree, lib)
        print("library created successfully")


'''
Función search
    Busca un valor en el Trie serializado, y retorna una lista con prioridad descendente de la palabra buscada
'''


def search(word):
    # Abro archivo contenedor del bin pickle
    with open('library.bin', 'rb') as lib:
        try:
            # Cargo el Trie en pickle
            trie = pickle.load(lib)

            # Busco la palabra en el Trie
            filesList = TSearch(trie, word)

            # Si no existe la palabra en el trie
            if(filesList == False):
                print("no document found")
            else:
                # Ordeno la lista con insertion sort
                InsertionSort(filesList)
                # Imprimo la lista
                printFilesList(filesList)

        # En caso de que el archivo este vacío (no se ha creado biblioteca)
        except EOFError:
            print("ERROR: Todavía no se ha creado una biblioteca")
            print(
                "Nota: 'python personal_library.py -create <local-path>' para crear una biblioteca")


'''
Función main
    Donde inicia el programa, verifica que los inputs por consola sean correctos y llama a las debidas funciones
'''


def main():
    inputValues = sys.argv

    # Si hay mas de 3 inputs, está mal ingresado
    if(len(inputValues) != 3):
        print("Código invalido")
        print("Intenta con:")
        print("     'python personal_library.py -create <local-path>' para crear una biblioteca")
        print("     'python personal_library.py -search <valor>' para buscar en una biblioteca")
    else:
        paramValue = String(inputValues[1])
        # Validación de los argumentos de búsqueda
        if(strcmp((paramValue), String('-create'))):
            # Segundo argumento es el path
            path = inputValues[2]

            #  Si existe el path
            if(os.path.exists(path)):
                # Llamo a la función create, con el path
                create(path)
            else:
                print("El directorio que ha ingresado es inválido o no existe")
                print("Intente con:")
                print(
                    "   Directorio absoluto, por ejemplo: C:/directorio/a/la/carpeta")
                print(
                    "   Directorio relativo (si está en la misma carpeta del programa), por ejemplo: directorio")
        elif(strcmp((paramValue), String('-search'))):
            # Segundo argumento es la búsqueda
            searchValue = inputValues[2]
            # Llamo a la función search, con la búsqueda
            search(searchValue)
        else:
            print("Ingrese un argumento válido ('-create' o '-search')")


# Call a la función principal
if __name__ == '__main__':
    main()
