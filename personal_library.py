# Imports manipulación de archivos
import sys
import os
# Import para serialización de datos
import pickle
# Imports propios
from linkedlist import *
from algo1 import *


class testObject():
    id = None
    name = None


def create(path):
    '''
        AVISO: por ahora solo funciona con un path exacto, arreglar para que funcione con path del directorio actual
    '''
    # Arreglo con los archivos del directorio
    libraryFiles = os.listdir(path)

    # Recorro los archivos del directorio
    for file in libraryFiles:
        '''
            AVISO: verificar extensión de los archivos que sea .txt
        '''
        with open(path + "\\" + file, 'r', encoding='utf-8') as currentFile:
            fileLines = currentFile.readlines()

            # Por archivo, línea por línea
            for line in fileLines:
                # Convierto a String✨ de Algo 1
                line = String(line)
                lineLength = len(line)
                word = String("")

                for i in range(0, lineLength):
                    if(line[i] == " " or line[i] == "," or line[i] == "."):
                        if(len(word) != 0):
                            '''
                            insert en el trie por palabra
                            '''
                            # print(word)
                        word = String("")
                    else:
                        word = concat(word, String(line[i]))

        '''
        Empezando a integrar pickle..
        '''

        test = testObject()
        test.id = 123
        test.name = 'test'

        with open('library.bin', 'bw') as lib:
            pickle.dump(test, lib)


def search(text):
    # Abro archivo contenedor del bin pickle
    with open('library.bin', 'rb') as lib:
        try:
            trie = pickle.load(lib)
            '''
                implementar busqueda en trie devuelto por pickle
            '''
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
                print("El directorio que ha ingresado es inválido")
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
