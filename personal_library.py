# Imports manipulación de archivos
import sys
import os
# Import para serialización de datos
import pickle
# Imports propios
from linkedlist import *
from algo1 import *
from main_structures import *


def isTextFile(filename):
    filenameLength = len(filename)
    # Si la longitud del filename es menor a 4, no tiene extensión
    if(filenameLength < 4):
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


def create(path):
    # Arreglo con los archivos del directorio
    libraryFiles = os.listdir(path)
    amountFiles = len(libraryFiles)
    # Si no hay archivos en la biblioteca
    if(amountFiles == 0):
        print("No hay archivos en la biblioteca")
        return

    # Creo Trie
    wordsTree = Trie()

    # Recorro los archivos del directorio
    for file in libraryFiles:
        # Solo leo archivo si es TXT
        if(isTextFile(file)):
            with open(path + "\\" + file, 'r', encoding='utf-8') as currentFile:
                print(currentFile)
                fileLines = currentFile.readlines()

                # Por archivo, línea por línea
                for line in fileLines:
                    # Convierto a String✨ de Algo 1
                    line = String(line)
                    lineLength = len(line)
                    word = String("")

                    for i in range(0, lineLength):
                        '''
                            Caractéres especiales: @ " ' , ´ { } ! $ % & / \ ( ) [ ] * = ° | : ; < > - _ ^ # ~
                        '''
                        if(line[i] == " " or line[i] == "," or line[i] == "."):
                            if(len(word) != 0):
                                # Insert de palabra en el árbol                             
                                TInsert(wordsTree, word, file)
                            word = String("")
                        else:
                            word = concat(word, String(line[i]))
    # Guardo trie en pickle
    with open('library.bin', 'bw') as lib:
        pickle.dump(wordsTree, lib)


def search(text):
    # Abro archivo contenedor del bin pickle
    with open('library.bin', 'rb') as lib:
        try:
            # Cargo el Trie en pickle
            trie = pickle.load(lib)          

            list = TSearch(trie,text)
            print(list.head.nextNode)
            listPrint(TSearch(trie,text))
        # En caso de que el archivo este vacío (no se ha creado biblioteca)
        except EOFError:
            print("ERROR: Todavía no se ha creado una biblioteca")
            print(
                "Nota: 'python personal_library.py -create <local-path>' para crear una biblioteca")


def main():
    if(len(sys.argv) != 3):
        print("Código invalido")
        print("Intenta con:")
        print("     'python personal_library.py -create <local-path>' para crear una biblioteca")
        print("     'python personal_library.py -search <valor>' para buscar en una biblioteca")
    else:
        paramValue = sys.argv[1]
        # Validación del argumento de búsqueda
        if(paramValue == '-create'):
            path = sys.argv[2]
            if(os.path.exists(path)):
                create(path)
            else:
                print("El directorio que ha ingresado es inválido o no existe")
                print("Intente con:")
                print(
                    "   Directorio absoluto, por ejemplo: C:/directorio/a/la/carpeta")
                print(
                    "   Directorio relativo (si está en la misma carpeta del programa), por ejemplo: directorio")
        elif(paramValue == '-search'):
            searchValue = sys.argv[2]

            search(searchValue)
        else:
            # Argumento no es ni -create o -search
            print("Ingrese un argumento válido ('-create' o '-search')")

        # Si el path ingresado existe


# Call a la función principal
if __name__ == '__main__':
    main()
