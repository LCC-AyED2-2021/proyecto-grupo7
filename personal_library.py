# Imports manipulación de archivos
import sys
import os
# Imports propios
from linkedlist import *
from algo1 import *


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
                print(lineLength)
                word = String("")

                for i in range(0, lineLength):
                    if(line[i] == " " or line[i] == "," or line[i] == "."):
                        if(len(word) != 0):
                            '''
                            insert en el trie por palabra
                            '''
                            print(word)
                        word = String("")
                    else:
                        word = concat(word, String(line[i]))


def search(text):
    print("Buscando en biblioteca")

# void


def main():
    if(len(sys.argv) != 3):
        print("Código invalido")
        print("Intenta con:")
        print("     'python personal_library.py -create <local-path>' para crear una biblioteca")
        print("     'python personal_library.py -search <valor>' para buscar en una biblioteca")
    else:
        path = sys.argv[2]
        # Si el path ingresado existe
        if(os.path.exists(path)):
            # Validación del argumento de búsqueda
            if(sys.argv[1] == '-create'):
                create(sys.argv[2])
            elif(sys.argv[2] == '-search'):
                search(sys.argv[2])
            else:
                # Argumento no es ni -create o -search
                print("Ingrese un argumento válido ('-create' o '-search')")
        else:
            print("El directorio que ha ingresado es inválido")


# Call a la función principal
if __name__ == '__main__':
    main()
