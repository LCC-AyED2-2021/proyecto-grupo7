import sys
import os


def create(path):
    # print(path)
    '''
        AVISO: por ahora solo funciona con un path exacto, arreglar para que funcione con path del directorio actual
    '''
    libraryFiles = os.listdir(path)

    for file in libraryFiles:
        '''
            AVISO: verificar extensión de los archivos que sea .txt
        '''
        with open(path + "\\" + file, 'r') as currentFile:
            print(currentFile.read())


def search(text):
    print("Buscando en biblioteca")


if(len(sys.argv) < 2):
    print("Código invalido")
else:
    # Verificación de argumentos de consola
    if(sys.argv[1] == '-create'):
        create(sys.argv[2])
    elif(sys.argv[2] == '-search'):
        search(sys.argv[2])
