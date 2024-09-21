import re
from LinkedList import LinkedList

palabrasReservadas = ["funct", "var", "ent", "cad", "flot", "bool", "verdadero", "falso", "const", "si", "o", "entonces", "para", "en rango", "mostrar", "escribir"]

def preProcesator():

    # Validate if the archive exist.

    try:

        file = open("example.txt", "r")
        noComment = ''

        # Delete comments.

        for line in file:

            noComment = noComment + line.split('//')[0]


        # Create the new file.

        newFileName = "out.txt"

        newFile = open(newFileName, "w")

        # Delete white spaces.

        newFile.write(noComment.rstrip() + '\n')

        return newFileName

    except:

        print('No data')

# Print each char in the text file.

def readFile(fileName):

    try:

        file = open(fileName, "r")

        print("Print each character.")

        for line in file:

            for char in line:

                print(char)

    except:

        print("Unexisted data!")


# Main function.

if __name__ == "__main__":

    fileName = preProcesator()

    readFile(fileName)
    
    lista = LinkedList()
    
