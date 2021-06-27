# Imports manipulación de archivos
import sys
import os
# Import para serialización de datos
import pickle
# Imports propios
# from linkedlist import *
from algo1 import *
from main_structures import *
from hash_structure import *
from insertionsort_structure import InsertionSort

# BORRAR
import time

sys.setrecursionlimit(10000)


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


def createImportantCharHash():
    hashTable = Array(255, LinkedList())
    insertHash(hashTable, " ")
    insertHash(hashTable, " ")
    insertHash(hashTable, "\n")
    return hashTable


def createSpecialCharsHash():
    hashTable = Array(255, LinkedList())
    insertHash(hashTable, " ")
    insertHash(hashTable, " ")
    insertHash(hashTable, " ")
    # insertHash(hashTable, "\n")
    insertHash(hashTable, '"')
    insertHash(hashTable, ',')
    insertHash(hashTable, '.')
    insertHash(hashTable, '-')
    insertHash(hashTable, '¡')
    insertHash(hashTable, '!')
    insertHash(hashTable, '¿')
    insertHash(hashTable, '?')
    insertHash(hashTable, '[')
    insertHash(hashTable, ']')
    insertHash(hashTable, '{')
    insertHash(hashTable, '}')
    insertHash(hashTable, '(')
    insertHash(hashTable, ')')
    insertHash(hashTable, '|')
    insertHash(hashTable, '¬')
    insertHash(hashTable, '°')
    insertHash(hashTable, '#')
    insertHash(hashTable, '^')
    insertHash(hashTable, '~')
    insertHash(hashTable, '/')
    insertHash(hashTable, ':')
    insertHash(hashTable, ';')
    insertHash(hashTable, '@')
    insertHash(hashTable, '*')
    insertHash(hashTable, '+')
    insertHash(hashTable, '_')
    insertHash(hashTable, '<')
    insertHash(hashTable, '>')
    insertHash(hashTable, '=')
    insertHash(hashTable, '`')
    insertHash(hashTable, '´')
    insertHash(hashTable, '×')
    insertHash(hashTable, 'ƒ')
    insertHash(hashTable, 'ª')
    insertHash(hashTable, 'º')
    insertHash(hashTable, '®')
    insertHash(hashTable, '¢')
    insertHash(hashTable, '©')
    insertHash(hashTable, '╣')
    insertHash(hashTable, '║')
    insertHash(hashTable, '╗')
    insertHash(hashTable, '╝')
    insertHash(hashTable, '┤')
    insertHash(hashTable, '│')
    insertHash(hashTable, '▓')
    insertHash(hashTable, '▒')
    insertHash(hashTable, '░')
    insertHash(hashTable, '»')
    insertHash(hashTable, '«')
    insertHash(hashTable, '¼')
    insertHash(hashTable, '½')
    insertHash(hashTable, '¾')
    insertHash(hashTable, '└')
    insertHash(hashTable, '┴')
    insertHash(hashTable, '┬')
    insertHash(hashTable, '├')
    insertHash(hashTable, '─')
    insertHash(hashTable, '┼')
    insertHash(hashTable, '╚')
    insertHash(hashTable, '╔')
    insertHash(hashTable, '╩')
    insertHash(hashTable, '╦')
    insertHash(hashTable, '╠')
    insertHash(hashTable, '═')
    insertHash(hashTable, '╬')
    insertHash(hashTable, '¤')
    insertHash(hashTable, 'ı')
    insertHash(hashTable, '┘')
    insertHash(hashTable, '┌')
    insertHash(hashTable, '█')
    insertHash(hashTable, '¯')
    insertHash(hashTable, '▄')
    insertHash(hashTable, '▀')
    insertHash(hashTable, '±')
    insertHash(hashTable, '≡')
    insertHash(hashTable, '¦')
    insertHash(hashTable, '§')
    insertHash(hashTable, '¶')
    insertHash(hashTable, '¸')
    insertHash(hashTable, 'Ì')
    insertHash(hashTable, '¨')
    insertHash(hashTable, '°')
    insertHash(hashTable, '·')
    insertHash(hashTable, '¹')
    insertHash(hashTable, '²')
    insertHash(hashTable, '³')
    insertHash(hashTable, '■')
    insertHash(hashTable, '→')
    insertHash(hashTable, 'Δ')

    return hashTable


def create(path):
    # Arreglo con los archivos del directorio
    libraryFiles = os.listdir(path)
    amountFiles = len(libraryFiles)

    total = 0

    # Si no hay archivos en la biblioteca
    if(amountFiles == 0):
        print("No hay archivos en la biblioteca")
        return
    print("Creando la biblioteca..")
    # Creo Trie
    wordsTree = Trie()
    specialCharHash = createSpecialCharsHash()
    importantCharHash = createImportantCharHash()
    # Recorro los archivos del directorio
    for file in libraryFiles:
        # Solo leo archivo si es TXT
        if(isTextFile(file)):
            print('NUEVO ARCHIVO: ', file)
            # t0 = time.time()
            with open(path + "\\" + file, 'r', encoding='utf-8') as currentFile:
                fileLines = currentFile.readlines()

                line = String(fileLines[0])
                lineLength = len(line)
                word = String("")

                for line in fileLines:
                    # Convierto a String✨ de Algo 1
                    line = String(line)
                    lineLength = len(line)
                    word = String("")

                    for i in range(0, lineLength):
                    #     if(searchHash(specialCharHash, line[i]) != None):
                    #         if(len(word) != 0):
                    #             # Insert de palabra en el árbol
                    #             TInsert(wordsTree, word, file)
                    #         word = String("")
                    #     else:
                    #         word = concat(word, String(line[i]))
                    #         # if(i == lineLength-1 and searchHash(specialCharHash, line[i]) == None):
                    #         if(i == lineLength-1):
                    #             TInsert(wordsTree, word, file)
                        if(searchHash(specialCharHash, line[i]) != None):
                            if(len(word) > 0):
                                if(i == lineLength-1):
                                    TInsert(wordsTree, word, file)
                                    word = String("")
                                else:
                                    if(searchHash(importantCharHash, line[i]) != None):
                                        TInsert(wordsTree, word, file)
                                        word = String("")
                                    elif(searchHash(importantCharHash, line[i+1]) != None):
                                        TInsert(wordsTree, word, file)
                                        word = String("")
                                    else:
                                        word = concat(word, String(line[i]))
                        else:
                            word = concat(word, String(line[i]))
                            if(i == lineLength-1):
                                TInsert(wordsTree, word, file)
                                word = String("")
            # t1 = time.time()
            # total += (t1-t0)
            # print(t1-t0, 's')
    # print(total)
    # Guardo trie en pickle
    with open('library.bin', 'bw') as lib:
        pickle.dump(wordsTree, lib)
        print("library created successfully")


def search(text):
    # Abro archivo contenedor del bin pickle
    with open('library.bin', 'rb') as lib:
        try:
            # Cargo el Trie en pickle
            trie = pickle.load(lib)

            filesList = TSearch(trie, text)
            print(filesList)

            if(filesList == False):
                print("no document found")
            else:
                InsertionSort(filesList)
                printFilesList(filesList)

        # En caso de que el archivo este vacío (no se ha creado biblioteca)
        except EOFError:
            print("ERROR: Todavía no se ha creado una biblioteca")
            print(
                "Nota: 'python personal_library.py -create <local-path>' para crear una biblioteca")


def main():
    inputValues = sys.argv
    if(len(inputValues) != 3):
        print("Código invalido")
        print("Intenta con:")
        print("     'python personal_library.py -create <local-path>' para crear una biblioteca")
        print("     'python personal_library.py -search <valor>' para buscar en una biblioteca")
    else:
        paramValue = inputValues[1]
        # Validación del argumento de búsqueda
        if(paramValue == '-create'):
            path = inputValues[2]
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
            searchValue = inputValues[2]
            search(searchValue)
        else:
            # Argumento no es ni -create o -search
            print("Ingrese un argumento válido ('-create' o '-search')")

        # Si el path ingresado existe


# Call a la función principal
if __name__ == '__main__':
    main()
